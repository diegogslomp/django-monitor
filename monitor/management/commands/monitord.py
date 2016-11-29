from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.utils import DatabaseError
from monitor.models import Log, Host
from monitor.settings import DAYS_FROM_DANGER_TO_WARNING, DAYS_FROM_INFO_TO_SUCCESS, WAIT_FOR_NEXT
import subprocess
import time
import datetime
import logging


class Command(BaseCommand):
    args = ''
    help = 'Monitor Daemon for Monitor hosts'

    def handle(self, *args, **options):

        logger = logging.getLogger(__name__)
        logger.info('Monitord started')

        while True:

            for host in Host.objects.all():

                now = timezone.now()
                host.last_check = now

                not_pinging = subprocess.call('ping %s -c 1 -W 2 -q > /dev/null 2>&1' % host.ipv4, shell=True)

                if not_pinging:
                    logger.info('Host %s is down', host.ipv4)
                    status_tmp = Host.DANGER
                    # if already whithout connection in 5 (default) or more days, 'warning' status
                    if host.status in (Host.WARNING, Host.DANGER) and host.last_status_change <= \
                            (now - datetime.timedelta(days=DAYS_FROM_DANGER_TO_WARNING)):
                        status_tmp = Host.WARNING
                else:
                    logger.info('Host %s is up', host.ipv4)
                    status_tmp = Host.INFO
                    # if is already up and more than 1 (default) day, 'success' status
                    if host.status in (Host.SUCCESS, Host.INFO) and host.last_status_change <= \
                            (now - datetime.timedelta(days=DAYS_FROM_INFO_TO_SUCCESS)):
                        status_tmp = Host.SUCCESS

                # Update host if status changed
                if host.status != status_tmp:
                    # Don't change last updated time for warning or success changes
                    if status_tmp != Host.WARNING and status_tmp != Host.SUCCESS:
                        host.last_status_change = now
                        Log.objects.create(host=host, status=status_tmp, status_change=now)
                    host.status = status_tmp

                # If the host still in the db, save it
                try:
                    # Update only time and status fields
                    host.save(update_fields=['last_check', 'last_status_change', 'status'])
                except DatabaseError as err:
                    logger.warning('%s %s', err, 'Deleted from database?')

                time.sleep(WAIT_FOR_NEXT)
