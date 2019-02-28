# Generated by Django 2.1.7 on 2019-02-27 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assets', '0003_auto_20190227_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancelog',
            name='Stamp',
        ),
        migrations.AddField(
            model_name='maintenancelog',
            name='DateStamp',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='maintenancelog',
            name='TimeStamp',
            field=models.TimeField(default='20:00'),
        ),
    ]
