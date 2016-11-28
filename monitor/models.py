from django.db import models
from .settings import DAYS_FROM_INFO_TO_SUCCESS, DAYS_FROM_DANGER_TO_WARNING
from django.utils import timezone


class Host(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ipv4 = models.GenericIPAddressField(protocol='IPv4')
    last_check = models.DateTimeField('last check', default=timezone.now)
    last_status_change = models.DateTimeField('last status change', default=timezone.now)

    DEFAULT = 0
    SUCCESS = 1
    INFO = 2
    WARNING = 3
    DANGER = 4

    STATUS_CHOICES = (
        (DEFAULT, 'default'),
        (SUCCESS, 'success'),
        (INFO, 'info'),
        (WARNING, 'warning'),
        (DANGER, 'danger'),
    )

    STATUS_INFO_CHOICES = (
        '',
        '',
        'Connected less than {0} day'.format(DAYS_FROM_INFO_TO_SUCCESS),
        'No connection more than {0} days'.format(DAYS_FROM_DANGER_TO_WARNING),
        'Connection lost',
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=DEFAULT)

    def status_info(self):
        return self.STATUS_INFO_CHOICES[self.status]

    def description_upper(self):
        return self.description.upper()

    def __str__(self):
        return self.name


class Log(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Host.STATUS_CHOICES)
    status_change = models.DateTimeField()

    def __str__(self):
        return self.host.name
