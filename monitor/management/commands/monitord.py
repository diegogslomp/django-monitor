from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from monitor.models import Host, Service
import paramiko, getpass, subprocess, time

class Command(BaseCommand):

    args = ''
    help = 'Monitor Daemon for Monitor hosts'

    def handle(self, *args, **options):

        # Set default status and get host list info
        host_list = Host.objects.all()

        for host in host_list:
            host.services_info = ''
            host.status = 'default'
            host.last_check = None
            host.save()
         
        # Get SSH info
        user = input('User: ')
        pw = getpass.getpass()

        while(True):
            
            for host in host_list:

                self.stdout.write('Hostname: %s' % host.name)
                host.last_check = timezone.now() 
                return_code = subprocess.call('ping %s -c 1 -W 2' % host.ipv4, shell=True) 
                
                # if ping get error
                if return_code:
                    host_status_tmp = 'danger'
                    host_services_info_tmp = 'No connection'
                else:
                    host_service_list = host.services.all()
                    host_status_tmp = 'success'
                    host_services_info_tmp = ''
                    if host_service_list.count() != 0:
                        # SSH connection
                        try:
                            self.stdout.write('Trying SSH connection to host: %s' % host.name)
                            client = paramiko.SSHClient()
                            client.set_missing_host_key_policy(paramiko.WarningPolicy())
                            client.connect(host.ipv4, username=user, password=pw)
                            chan = client.get_transport().open_session()
                            # for every service, check
                            for service in host_service_list:

                                cmd = service.verify_command
                                if cmd == '': break;
                                self.stdout.write('running %s' % cmd)
                                chan.exec_command(cmd)
                                return_code = chan.recv_exit_status()
                                self.stdout.write('exit status: %s' % return_code)
                                # if service verify get error change html state and info
                                if not str(return_code) == '0':
                                    if host_status_tmp == 'success' or 'warning':
                                        host_services_info_tmp = 'Error: '
                                    else:
                                        host_services_info_tmp += str(', ')
                                    host_status_tmp = 'danger'
                                    host_services_info_tmp += str('%s' % service.name)

                            client.close()
                        except:
                                self.stdout.write('Error: No SSH connection on host: %s' % host.name)
                                host_services_info_tmp = 'No SSH connection'
                                host_status_tmp = 'warning'
                #Update host
                host.status = host_status_tmp
                host.services_info = host_services_info_tmp
                host.save()
                time.sleep(1)

            # Update host list
            host_list = Host.objects.all()

