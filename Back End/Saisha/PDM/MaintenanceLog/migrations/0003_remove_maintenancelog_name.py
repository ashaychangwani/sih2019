# Generated by Django 2.1.7 on 2019-02-27 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MaintenanceLog', '0002_maintenancelog_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancelog',
            name='Name',
        ),
    ]
