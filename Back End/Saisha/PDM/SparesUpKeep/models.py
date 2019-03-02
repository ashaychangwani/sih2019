import datetime

from django.db import models

# Create your models here.

class Spares(models.Model):
    MachineID = models.PositiveIntegerField()
    ComponentName = models.CharField(max_length=250)
    Count = models.PositiveIntegerField()

    def __str__(self):
        return str(self.MachineID) + " - " + self.ComponentName + " - " + str(self.Count)

class Order(models.Model):
    MachineID = models.PositiveIntegerField(default=0)
    Customer = models.CharField(max_length=250,default="")
    ComponentName = models.CharField(max_length=250)
    Count = models.PositiveIntegerField()
    CostOfPart = models.FloatField(default=0.0)
    TotalAmount = models.FloatField(default=0.0)
    Date2 = models.DateField(default=datetime.date.today())

    def __str__(self):
        return str(self.MachineID) + " - " + self.ComponentName + " - " + str(self.TotalAmount)