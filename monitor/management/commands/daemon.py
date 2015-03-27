from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from monitor.models import Host, Service
import paramiko, getpass, subprocess, time

class Command(BaseCommand):

    args = ''
    help = 'Monitor Daemon for PMCS Monitor hosts'

    def handle(self, *args, **options):

        # Set default status and get host list info
        host_list = Host.objects.all()

        for host in host_list:
            host.services_info=''
            host.status=''
            host.last_check = None
            host.save()
         
        # Get SSH info
        user = raw_input("User: ")
        pw = getpass.getpass()

        while(True):
            
            for host in host_list:

                self.stdout.write('Hostname: "%s"' % host.name)
                host.last_check = timezone.now() 
                return_code = subprocess.call('ping %s -c 1 -W 2' % host.ipv4, shell=True) 

                # if ping get error
                if return_code:
                    host.status = "danger"
                    host.services_info = "No connection"
                    host.save()
                    break

                host_service_list = host.services.all()
                host_status_tmp = "success"
                host.services_info = ""

                for service in host_service_list:

                    cmd = service.verify_command

                    if cmd == '':
                        break

                    self.stdout.write('Service Verify Command: "%s"' % cmd)

                    # SSH connection...
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.WarningPolicy())
                    client.connect(host.ipv4, username=user, password=pw)
                    chan = client.get_transport().open_session()
                    self.stdout.write("running '%s'" % cmd)
                    chan.exec_command(cmd)
                    return_code =  chan.recv_exit_status()
                    self.stdout.write("exit status: %s" % return_code)
                    client.close()

                    # if service verify get error change html state and info
                    if return_code:

                        if host_status_tmp == "success":
                            host.services_info = "Error: ";
                        else:
                            host.services_info += str(", ")

                        host_status_tmp="danger"
                        host.services_info += str("%s" % service.name)

                host.status = host_status_tmp
                host.save()
                time.sleep(1)

            # Update host list
            host_list = Host.objects.all()

            # for oneloop tests
            #break

