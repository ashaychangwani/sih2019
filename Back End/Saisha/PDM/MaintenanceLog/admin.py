from django.contrib import admin

# Register your models here.
from .models import MaintenanceLog, PendingLog

admin.site.register(MaintenanceLog)
admin.site.register(PendingLog)