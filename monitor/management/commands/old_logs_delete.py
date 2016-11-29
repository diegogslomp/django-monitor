from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.utils import DatabaseError
from monitor.models import Log, Host
from monitor.settings import DAYS_FROM_DANGER_TO_WARNING, DAYS_FROM_INFO_TO_SUCCESS, WAIT_FOR_NEXT, MAX_LOG_LINES
import subprocess
import time
import datetime
import logging


class Command(BaseCommand):
    args = ''
    help = 'Delete old log lines based on settings.MAX_LOG_LINES value'

    def handle(self, *args, **options):

        logger = logging.getLogger(__name__)
        logger.info('old_logs_delete started!')

        for host in Host.objects.all():
            host_to_del_logs = Log.objects.filter(host=host).order_by('-status_change')[MAX_LOG_LINES:]\
                                          .values_list("id", flat=True)
            Log.objects.exclude(pk__in=list(host_to_del_logs)).delete()
        logger.info('old_logs_delete finished!')
