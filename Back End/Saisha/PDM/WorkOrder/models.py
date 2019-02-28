from django.db import models

# Create your models here.

class WorkOrder(models.Model):
    WorkOrderNum = models.PositiveIntegerField(default=0)
    Description = models.CharField(max_length=250, default="")
    DateStamp = models.DateField(default='2011-10-01')
    StartTime = models.TimeField(default='20:00')
    EndTime = models.TimeField(default='21:00')
    Status = models.CharField(max_length=250, default="")
    Cost = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.MachineID) + " - " + self.ComponentName + " - " + str(self.Count)
