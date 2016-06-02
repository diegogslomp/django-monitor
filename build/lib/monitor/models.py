from django.db import models
from .settings import DAYS_FROM_INFO_TO_SUCCESS, DAYS_FROM_DANGER_TO_WARNING
from django.utils import timezone


class Host(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ipv4 = models.GenericIPAddressField(protocol='IPv4')
    last_check = models.DateTimeField('last check', default=timezone.now)
    last_status_change = models.DateTimeField('last status change', default=timezone.now)

    STATUS_CHOICES = (
        (0, 'default'),
        (1, 'success'),
        (2, 'info'),
        (3, 'warning'),
        (4, 'danger'),
    )

    STATUS_INFO_CHOICES = (
        '',
        '',
        'Connected less than {0} day'.format(DAYS_FROM_INFO_TO_SUCCESS),
        'More than {0} days without connection'.format(DAYS_FROM_DANGER_TO_WARNING),
        'No Connection',
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def status_info(self):
        return self.STATUS_INFO_CHOICES[self.status]

    def description_upper(self):
        return self.description.upper()

    def __str__(self):
        return self.name
