from django.core.management.base import BaseCommand
from monitor.models import Log, Host
from monitor.settings import MAX_LOG_LINES
import logging


class Command(BaseCommand):
    args = ''
    help = 'Delete old log lines based on settings.MAX_LOG_LINES value'

    def handle(self, *args, **options):

        logger = logging.getLogger(__name__)
        logger.info('old_logs_delete started!')

        for host in Host.objects.all():
            Log.objects.filter(pk__in=Log.objects.filter(host=host).order_by('-status_change').values_list('pk')[MAX_LOG_LINES:]).delete()

        logger.info('old_logs_delete finished!')
