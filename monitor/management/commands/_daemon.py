from django.core.management.base import BaseCommand, CommandError
from monitor.models import Host, Service
import paramiko, getpass, subprocess, time

class Command(BaseCommand):

    args = ''
    help = 'Monitor Daemon for PMCS Monitor hosts'

    def handle(self, *args, **options):

        user = raw_input("User: ")
        pw = getpass.getpass()

        while(True):

            host_list = Host.objects.all()
            for host in host_list:

                self.stdout.write('Hostname: "%s"' % host.name)
                return_code = subprocess.call('ping %s -c 1' % host.ipv4, shell=True) 

                if return_code:
                    host.status="danger"
                    break

                host_service_list = host.services.all()
                host_status_tmp = "success"

                for service in host_service_list:

                    self.stdout.write('Service Verify Command: "%s"' % service.verify_command)
                    # SSH connection...
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.WarningPolicy())
                    client.connect(host.ipv4, username=user, password=pw)
                    # Temp test ssh connection
                    while True:
                        cmd = raw_input("Command to run: ")
                        if cmd == "":
                            break
                        chan = client.get_transport().open_session()
                        self.stdout.write("running '%s'" % cmd)
                        chan.exec_command(cmd)
                        self.stdout.write("exit status: %s" % chan.recv_exit_status())
                    client.close()
                    # End Test

#                    return_code = subprocess.call(service.verify_command % host.ipv4, shell=True) 
#                    self.stdout.write('Returned Value: "%s"' % return_code)
#                    if service verify get error change html state and info
#                    if return_code:
#                        host.status.tmp="danger"
#
#                host.status = host_status_tmp
#                host.save()
#                time.sleep(1)

