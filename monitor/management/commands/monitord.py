from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.utils import DatabaseError
from monitor.models import Log, Host, Port
from monitor.settings.base import DAYS_FROM_DANGER_TO_WARNING, WAIT_FOR_NEXT, MAX_LOG_LINES
from monitor.settings.base import USER, PASSWORD
from telnetlib import Telnet
import subprocess
import time
import datetime
import logging


class Command(BaseCommand):
    args = ''
    help = 'Monitor Daemon for Monitor hosts'

    logger = logging.getLogger(__name__)
    status_tmp = ''
    status_info_tmp = ''
    now = None

    def status_handler(self, host):
        # if already whithout connection in 5 (default) or more days, 'warning' status
        if self.status_tmp == Host.DANGER and host.status in (Host.DANGER, Host.WARNING) and \
                host.last_status_change <= (self.now - datetime.timedelta(days=DAYS_FROM_DANGER_TO_WARNING)):
            self.status_tmp = Host.WARNING

        # Update host if status changed
        if host.status != self.status_tmp or host.status_info != self.status_info_tmp:
            self.logger.warning('Status and/or status info changed to host {0}'.format(host.ipv4))
            host.status = self.status_tmp
            host.status_info = self.status_info_tmp
            # Don't change last updated time for warning changes
            if self.status_tmp != Host.WARNING:
                host.last_status_change = self.now
                # Add new log
                Log.objects.create(host=host, status=self.status_tmp,
                                   status_info=self.status_info_tmp, status_change=self.now)
                # Remove old logs based on MAX_LOG_LINES
                Log.objects.filter(pk__in=Log.objects.filter(host=host).order_by('-status_change')
                                   .values_list('pk')[MAX_LOG_LINES:]).delete()

    def save_db(self, host):
        # If the host still in the db, save it
        try:
            # Update only time and status fields
            host.save(update_fields=['last_check', 'last_status_change', 'status', 'status_info'])
        except DatabaseError as err:
            self.logger.warning('{0} {1}'.format(err, 'Deleted from database?'))

    def telnet(self, host, host_ports):
        tn = Telnet(host.ipv4)
        tn.read_until(b"Username:")
        tn.write(USER.encode('ascii') + b"\n")
        tn.read_until(b"Password:")
        tn.write(PASSWORD.encode('ascii') + b"\n")
        # Wait prompt '->' for successful login or 'Username' for wrong credentials
        match_object = tn.expect([b"->", b"Username:"])[1]
        if match_object.group(0) == b"Username:":
            self.status_tmp = Host.DANGER
            self.status_info_tmp = 'Invalid telnet user or password'
            self.logger.warning('Telnet connection to {0} refused'.format(host.ipv4))
        else:
            self.logger.info('Successful telnet connection to {0}'.format(host.ipv4))
            for port in host_ports:
                tn_command = 'show port status {0}'.format(port.number)
                tn.write(tn_command.encode('ascii') + b"\n")
            tn.write(b"exit\n")
            # Filter telnet output lines
            for line in tn.read_all().decode('ascii').replace('\r', '').split('\n'):
                if 'no valid port' in line.lower() or 'invalid port' in line.lower():
                    self.logger.warning('Invalid port registered for host {0} ({1})'.format(host.ipv4, line))
                    self.status_tmp = Host.DANGER
                    self.status_info_tmp = 'Invalid port configured or port module is down'
                    continue
                for port in host_ports:
                    if port.number in line and 'show port status' not in line and 'down' in line.lower():
                        self.status_tmp = Host.DANGER
                        msg = 'Port {0} ({1}) is Down'.format(port.number, line.split()[1])
                        if self.status_info_tmp == 'Connected':
                            self.status_info_tmp = msg
                        else:
                            self.status_info_tmp += ', {0}'.format(msg)
        self.logger.info('Telnet finished.')

    def ping(self, host):
        is_pinging = not subprocess.call('ping {0} -c 1 -W 2 -q > /dev/null 2>&1'.format(host.ipv4), shell=True)
        if is_pinging:
            self.logger.info('Host {0} is up'.format(host.ipv4))
            self.status_tmp = Host.SUCCESS
            self.status_info_tmp = 'Connected'
        else:
            self.logger.info('Host {0} is down'.format(host.ipv4))
            self.status_tmp = Host.DANGER
            self.status_info_tmp = 'Connection Lost'
        return is_pinging

    def check_host(self, host):
        self.status_tmp = ''
        self.status_info_tmp = ''
        self.now = timezone.now()
        host.last_check = self.now
        if self.ping(host):
            host_ports = Port.objects.filter(host=host)
            if host_ports.count() > 0:
                self.logger.info('Registered ports found. Telnet connection started to {0}'.format(host.ipv4))
                self.telnet(host, host_ports)
        self.status_handler(host)
        self.save_db(host)

    def loop(self):
        while True:
            for host in Host.objects.all():
                self.check_host(host)
                time.sleep(WAIT_FOR_NEXT)

    def handle(self, *args, **options):
        self.logger.info('Monitord started')
        self.loop()
