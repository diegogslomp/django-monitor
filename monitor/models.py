from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    verify_command = models.CharField(max_length=200, blank=True)
    return_expected = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ipv4 = models.CharField(max_length=200)
    services = models.ManyToManyField(Service, blank=True)
    services_info = models.CharField(max_length=200, blank=True)
    last_check = models.DateTimeField('last check', null=True, blank=True)

    STATUS_CHOICES = (
        ('', 'Default'),
        ('success', 'Ok'),
        ('warning', 'Warning'),
        ('danger', 'Critical'),
        ('info', 'Info'),
    )
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='',
                              blank=True)

    def __str__(self):
        return self.name
