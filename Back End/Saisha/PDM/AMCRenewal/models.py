from datetime import date, datetime

from django.db import models

# Create your models here.

class AMC(models.Model):
    MachineID = models.IntegerField()
    Company = models.CharField(max_length=250, default="")
    Category = models.CharField(max_length=250, default="")
    Quantity = models.PositiveIntegerField(default=0)
    FactoryID = models.PositiveIntegerField(default=0)
    AMCCompany = models.CharField(max_length=250, default="")
    ExpiryDate = models.DateField(default='2011-10-01')

    def __str__(self):
        return str(self.machineID) + " - " + str(self.FactoryID) + " - " + str(self.AMCCompany)