from django.core.management.base import BaseCommand
from monitor.models import Host
from monitor.settings import WAIT_FOR_NEXT
import time
import logging
import re
import sys


class Command(BaseCommand):
    args = ''
    logger = logging.getLogger(__name__)
    help = 'Show gateways from all hosts'

    def main(self):
    
        for host in Host.objects.all():
            if not re.search(r'^RADIO', host.name) and host.isalive:
                gateway = str(host.check_gateway())
                sys.stdout.write('{:15} - {:15} - {}\n'.format(host.ipv4, gateway, host.name))

    def handle(self, *args, **options):
        self.logger.info('Show gateways started')
        self.main()
