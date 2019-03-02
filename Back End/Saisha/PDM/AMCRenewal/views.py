from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import AMC

def DisplayTable(request):
    amc = AMC.objects.all()
    context = {
        'amc': amc,
    }
    return HttpResponse(render(request, 'amc/amc.html', context))

def Form(request):
    if request.method == 'POST' :
        MachineID = request.POST.get('mid', False)
        Facility = request.POST.get('facility', False)
        ProductionLine = request.POST.get('prod', False)
        Factory = request.POST.get('fac', False)
        Frequency = request.POST.get('freq', False)
        Supplier = request.POST.get('sup', False)
        LastRenewal = request.POST.get('date', False)
        Details = request.POST.get('details', False)
        amc = AMC(MachineID=MachineID, Facility=Facility, Factory=Factory, ProductionLine=ProductionLine, Frequency=Frequency, Supplier=Supplier, LastRenewal=LastRenewal, Details=Details)
        print(MachineID)
        amc.save()

    return HttpResponse(render(request,'amc/amcform.html'),{})