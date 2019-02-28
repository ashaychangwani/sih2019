from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import MaintenanceLog


def maintenanceLog(request):
    maintenanceLog1 = MaintenanceLog.objects.all()
    context = {
        'maintenanceLog' : maintenanceLog1,
    }
    return HttpResponse(render(request, 'Maintenance.html', context))
