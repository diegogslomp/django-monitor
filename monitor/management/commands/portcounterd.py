from django.core.management.base import BaseCommand
from monitor.models import Host
from monitor.settings import WAIT_FOR_NEXT
import time
import logging


class Command(BaseCommand):
    args = ''
    logger = logging.getLogger(__name__)
    help = 'Monitor Port Errors from Hosts'

    def loop(self):
        while True:
            for host in Host.objects.all():
                host.check_port_counters()
                time.sleep(WAIT_FOR_NEXT)

    def handle(self, *args, **options):
        self.logger.info('Portcounterd started')
        self.loop()
