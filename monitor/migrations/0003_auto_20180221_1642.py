# Generated by Django 2.0.2 on 2018-02-21 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20180221_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='status_info',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
