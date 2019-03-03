from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import MaintenanceLog, PendingLog


def maintenanceLog(request):
    maintenanceLog1 = MaintenanceLog.objects.all()
    context = {
        'maintenanceLog' : maintenanceLog1,
    }
    return HttpResponse(render(request, 'maintenance/Maintenance.html', context))

def pendingLog(request):
    pendingLog1 = PendingLog.objects.all()
    context = {
        'pendingLog' : pendingLog1,
    }
    if request.method == "POST":
        i = request.POST.get('c1', False)
        print(i)
    return HttpResponse(render(request, 'maintenance/pending.html', context))
