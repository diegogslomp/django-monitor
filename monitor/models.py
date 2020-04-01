from django.db import models
from django.utils import timezone
from .settings import USER, PASSWORD, TELNET_TIMEOUT
from .settings import DAYS_FROM_DANGER_TO_WARNING, MAX_LOG_LINES
import datetime
import logging
import re
import subprocess
import telnetlib


class Host(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    ipv4 = models.GenericIPAddressField(protocol='IPv4')
    last_check = models.DateTimeField('last check', default=timezone.now)
    last_status_change = models.DateTimeField('last status change', default=timezone.now)
    status_info = models.CharField(max_length=200, blank=True, default='')
    DEFAULT = 0
    SUCCESS = 1
    INFO = 2
    WARNING = 3
    DANGER = 4
    STATUS_CHOICES = (
        (DEFAULT, 'secondary'),
        (SUCCESS, 'positive'),
        (INFO, 'primary'),
        (WARNING, 'warning'),
        (DANGER, 'negative'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=DEFAULT)
    logger = logging.getLogger(__name__)

    def __str__(self):
        return self.name

    @property
    def ports(self):
        return Port.objects.filter(host=self)

    @property
    def monitored_ports(self):
        return Port.objects.filter(host=self, is_monitored=True)

    @property
    def isalive(self):
        return not subprocess.call('ping {} -c 1 -W 2 -q > /dev/null 2>&1'\
                                    .format(self.ipv4), shell=True)

    def log(self, message, level='debug'):
        if level == 'info':
            self.logger.info('{:14} {}'.format(self.ipv4, message))
        elif level == 'warning':
            self.logger.warning('{:14} {}'.format(self.ipv4, message))
        else:
            self.logger.debug('{:14} {}'.format(self.ipv4, message))

    def check_monitored_ports_status(self):
        '''Filter telnet manually added monitored ports'''
        if self.monitored_ports.count() > 0:

            def telnet_commands_monitored_ports():
                commands = []
                for port in self.monitored_ports:
                    commands.append('show port status {0}'.format(port.number))
                return commands

            self.log('Telnet to check monitored ports')
            telnet_output = self.telnet(telnet_commands_monitored_ports())    
            if telnet_output != '':
                for line in telnet_output.lower().replace('\r', '').split('\n'):
                    if re.search(r'[no ,in]valid', line):
                        self.status = self.DANGER
                        self.status_info = 'Invalid port registered or module is Down'
                        self.log(self.status_info, 'warning')
                        continue
                    for port in self.monitored_ports:
                        if re.search(r'{}.*down'.format(port.number), line):
                            self.status = self.DANGER
                            msg = 'Port {} ({}) is Down'.format(port.number, line.split()[1])
                            if self.status_info == 'Connected':
                                self.status_info = msg
                            else:
                                self.status_info += ', {}'.format(msg)
                            self.log(self.status_info)

    def check_port_counters(self):
        '''Filter telnet port counters, create ports and change status'''
        if self.isalive and not re.search(r'^RADIO', self.name):
            now = timezone.now()
            telnet_output = self.telnet(['show port counters'])
            if telnet_output != '':
                port_object = None
                for line in telnet_output.lower().replace('\r', '').split('\n'):
                    # Create port if not exists
                    if re.search(r'^port:', line):
                        port_number = line.split()[1]
                        self.log('Filtered Port: {}'.format(port_number))
                        port_object = Port.objects.get_or_create(host=self, number=port_number)[0]
                    elif re.search(r'^port :', line):
                        port_number = line.split()[2]
                        self.log('Filtered Port: {}'.format(port_number))
                        port_object = Port.objects.get_or_create(host=self, number=port_number)[0]
                    # Update counter and status
                    elif re.search(r'^in errors', line):
                        error_counter = int(line.split()[2])
                        self.log('Filtered Counter: {}'.format(error_counter))
                        self.log('Old Counter: {}'.format(port_object.error_counter))
                        # Only save updated fields
                        update_fields=[]
                        # If conter updated, change var and status
                        if error_counter != port_object.error_counter:
                            port_object.error_counter = error_counter
                            port_object.counter_last_change = now
                            port_object.counter_status = Host.DANGER
                            update_fields.extend(['error_counter', 'counter_last_change', 'counter_status']) 
                            # Add port log if counter changed
                            port_object.update_log()
                            self.log('Counter updated to: {}'.format(error_counter))
                        else:
                            old_counter_status = port_object.counter_status
                            delta_1_day = now - datetime.timedelta(days=1)
                            if port_object.counter_last_change <= delta_1_day:
                                port_object.counter_status = self.WARNING
                            delta_5_days = now - datetime.timedelta(days=5)
                            if port_object.counter_last_change <= delta_5_days:
                                port_object.counter_status = self.SUCCESS
                            if old_counter_status != port_object.counter_status:
                                update_fields.extend(['counter_status'])
                        if len(update_fields) > 0:
                            try:
                                port_object.save(update_fields=update_fields)
                                self.log('Save port log to database')
                            except Exception as ex:
                                self.log(ex, 'warning')
                        port_object = None

    def check_gateway(self):
        '''Filter gateway from telnet output'''
        if self.isalive and not re.search(r'^RADIO', self.name):
            now = timezone.now()
            telnet_output = self.telnet(['show ip route'])
            if telnet_output != '':
                for line in telnet_output.lower().replace('\r', '').split('\n'):
                    if re.search(r'0.0.0.0', line):
                        self.log('Gateway telnet line: {}'.format(line))
                        if re.search('^\s*s', line):
                            self.log('Filtered gateway: {}'.format(line.split()[4]))
                            return line.split()[4]
                        else:                            
                            self.log('Filtered gateway: {}'.format(line.split()[1]))
                            return line.split()[1]


    def telnet(self, commands):
        '''Telnet connection and get registered ports status'''
        self.log('Telnet started')
        telnet_output = ''
        try:
            tn = telnetlib.Telnet(self.ipv4, timeout=TELNET_TIMEOUT)
            tn.read_until(b"Username:")
            tn.write(USER.encode('ascii') + b"\n")
            tn.read_until(b"Password:")
            tn.write(PASSWORD.encode('ascii') + b"\n")
            # '->' for successful login or 'Username' for wrong credentials
            match_object = tn.expect([b"->", b"Username:"])[1]
            if match_object.group(0) == b"Username:":
                self.status = self.DANGER
                self.status_info = 'Invalid telnet user or password'
                self.log(self.status_info, 'warning')
            else:
                for tn_command in commands:
                    self.log(tn_command)
                    tn.write(tn_command.encode('ascii') + b"\n")
                tn.write(b"exit\n")
                self.log('Telnet finished')
                telnet_output = tn.read_all().decode('ascii')
        except Exception as ex:
            self.status = self.DANGER
            self.status_info = 'Telnet error: {0}'.format(ex)
            self.log(self.status_info, 'warning')
        finally:
            return telnet_output

    def check_ping(self):
        '''Ping host, then telnet if there are registered ports'''
        if self.isalive:
            self.status = self.SUCCESS
            self.status_info = 'Connected'
        else:
            self.status = self.DANGER
            self.status_info = 'Connection Lost'
        self.log(self.status_info)

    def update_log(self):
        '''Add new host log and remove old logs based on MAX_LOG_LINES'''
        try:
            HostLog.objects.create(host=self, status=self.status,
                               status_info=self.status_info, status_change=self.last_status_change)
            HostLog.objects.filter(pk__in=HostLog.objects.filter(host=self).order_by('-status_change')
                                .values_list('pk')[MAX_LOG_LINES:]).delete()
        except Exception as ex:
            self.log(ex, 'warning')

    def check_and_update(self):
        '''The 'main' function of monitord, check/update host and logs'''
        now = timezone.now()
        self.last_check = now
        # Only update changed fields in DB
        update_fields = ['last_check']
        # Store old data before change it
        old_status_info = self.status_info
        self.check_ping()
        self.check_monitored_ports_status()
        #  if status info changed, update status and logs
        if old_status_info != self.status_info:
            self.log('Status info changed from "{}" to "{}"'
                     .format(old_status_info, self.status_info))
            self.last_status_change = now
            update_fields.extend(['last_status_change', 'status', 'status_info'])
            self.update_log()
        # check if change the status from danger to warning status
        elif self.status == self.DANGER:
            delta_limit_to_warning_status = now - datetime.timedelta(days=DAYS_FROM_DANGER_TO_WARNING)
            if self.last_status_change <= delta_limit_to_warning_status:
                self.status = self.WARNING
                update_fields.extend(['status'])
        # Save only if the host was not deleted while in buffer
        try:
            self.save(update_fields=update_fields)
        except Exception as ex:
            self.log(ex, 'warning')


class HostLog(models.Model):
    '''Host Logs showed in host detail view'''
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Host.STATUS_CHOICES, default=Host.DEFAULT)
    status_change = models.DateTimeField()
    status_info = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.host.name


class Port(models.Model):
    '''Ports used to check status using telnet'''
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    is_monitored = models.BooleanField(default=False)
    counter_status = models.IntegerField(choices=Host.STATUS_CHOICES, default=Host.DEFAULT)
    counter_last_change = models.DateTimeField('last status change', default=timezone.now)
    error_counter = models.IntegerField(default=0)

    def update_log(self):
        '''Add new port log and remove old logs based on MAX_LOG_LINES'''
        try:
            PortLog.objects.create(port=self, host=self.host, counter_status=self.counter_status, 
                                   counter_last_change=self.counter_last_change,
                                   error_counter=self.error_counter)
            PortLog.objects.filter(pk__in=PortLog.objects.filter(port=self).order_by('-counter_last_change')
                                .values_list('pk')[MAX_LOG_LINES:]).delete()
        except Exception as ex:
            Host.log(ex, 'warning')

    def __str__(self):
        return self.number


class PortLog(models.Model):
    '''Port Logs showed in host detail view'''
    port = models.ForeignKey(Port, on_delete=models.CASCADE, null=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE, null=True)
    counter_status = models.IntegerField(choices=Host.STATUS_CHOICES, default=Host.DEFAULT)
    counter_last_change = models.DateTimeField('last status change', default=timezone.now)
    error_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.port.number
