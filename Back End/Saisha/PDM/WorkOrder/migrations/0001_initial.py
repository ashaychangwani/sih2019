# Generated by Django 2.1.7 on 2019-02-27 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorkOrderNum', models.PositiveIntegerField(default=0)),
                ('Description', models.CharField(default='', max_length=250)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('StartTime', models.TimeField(default='20:00')),
                ('EndTime', models.TimeField(default='21:00')),
                ('Status', models.CharField(default='', max_length=250)),
                ('Cost', models.FloatField(default=0.0)),
            ],
        ),
    ]
