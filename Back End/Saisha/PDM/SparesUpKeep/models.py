from django.db import models

# Create your models here.

class Spares(models.Model):
    MachineID = models.PositiveIntegerField()
    ComponentName = models.CharField(max_length=250)
    Count = models.PositiveIntegerField()

    def __str__(self):
        return str(self.MachineID) + " - " + self.ComponentName + " - " + str(self.Count)
