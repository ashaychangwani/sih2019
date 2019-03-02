from django.db import models

# Create your models here.

class AMC(models.Model):
    MachineID = models.IntegerField()
    Facility = models.CharField(max_length=250, default="", null=True)
    Factory = models.CharField(max_length=250, default="", null=True)
    ProductionLine = models.CharField(max_length=250, default="", null=True)
    Frequency = models.CharField(max_length=200, default="", null=True)
    Supplier = models.CharField(max_length=250, default="", null=True)
    LastRenewal = models.DateField(default='2011-10-01')
    Details = models.CharField(max_length=500, default="", null=True)

    def __str__(self):
        return str(self.MachineID) + " - " + str(self.Factory) + " - " + str(self.Supplier)