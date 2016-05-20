from django.core.management.base import BaseCommand
from django.utils import timezone
from monitor.models import Host
from monitor.settings import DAYS_FROM_DANGER_TO_WARNING, DAYS_FROM_INFO_TO_SUCCESS, WAIT_FOR_NEXT
import subprocess
import time
import datetime


class Command(BaseCommand):
    args = ''
    help = 'Monitor Daemon for Monitor hosts'

    def handle(self, *args, **options):

        while True:

            host_list = Host.objects.all()

            for host in host_list:

                now = timezone.now()
                not_pinging = subprocess.call('ping %s -c 1 -W 2 -q > /dev/null 2>&1' % host.ipv4, shell=True)

                if not_pinging:
                    status_tmp = 4  # 'danger'
                    # if already whithout connection in 5 (default) or more days, 'warning' status
                    if host.status in (3, 4) and host.last_status_change <= \
                            (now - datetime.timedelta(days=DAYS_FROM_DANGER_TO_WARNING)):
                        status_tmp = 3  # 'warning'
                else:
                    status_tmp = 2  # 'info'
                    # if is already up and more than 1 (default) day, 'success' status
                    if host.status in (1, 2) and host.last_status_change <= \
                            (now - datetime.timedelta(days=DAYS_FROM_INFO_TO_SUCCESS)):
                        status_tmp = 1  # 'success'

                # Update host if status changed
                if host.status != status_tmp:
                    # Don't change last updated time for warning or success changes
                    if status_tmp != 3 and status_tmp != 1:
                        host.last_status_change = now
                    host.status = status_tmp

                # If the host still in the db, save it
                if host in Host.objects.all():
                    host.last_check = now
                    host.save()

                time.sleep(WAIT_FOR_NEXT)
