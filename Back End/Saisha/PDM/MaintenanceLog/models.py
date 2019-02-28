import datetime
from django.db import models

# Create your models here.

class MaintenanceLog(models.Model):
    MachineID = models.PositiveIntegerField()
    DateStamp = models.DateField(("Date"), default=datetime.date.today)
    TimeStamp = models.TimeField(default='20:00')
    Details = models.CharField(max_length=500)
    Comments = models.CharField(max_length=1000)

    def __str__(self):
        return "MachineID " + str(self.MachineID) + " - " + str(self.DateStamp) + " - " + str(self.TimeStamp)