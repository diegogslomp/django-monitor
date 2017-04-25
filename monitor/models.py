from django.db import models
from django.utils import timezone


class Host(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ipv4 = models.GenericIPAddressField(protocol='IPv4')
    last_check = models.DateTimeField('last check', default=timezone.now)
    last_status_change = models.DateTimeField('last status change', default=timezone.now)
    status_info = models.CharField(max_length=200, blank=True, default='')

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

    status = models.IntegerField(choices=STATUS_CHOICES, default=DEFAULT)

    def __str__(self):
        return self.name


class Log(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Host.STATUS_CHOICES)
    status_change = models.DateTimeField()
    status_info = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.host.name


class Port(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number
