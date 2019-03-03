import datetime

from django.db import models

# Create your models here.

# Blueprint for your database
# What tables you'll need - each class is a table
# How you're gonna store it

class Asset(models.Model):
    Name = models.CharField(max_length=250)
    FacilityName = models.CharField(max_length=250)
    FactoryNum = models.CharField(max_length=250)
    Prodline = models.CharField(max_length=250)
    MachineID = models.PositiveIntegerField()

    def __str__(self):
        return str(self.MachineID) + " - " + self.Name
