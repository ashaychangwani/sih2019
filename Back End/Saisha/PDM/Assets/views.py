from django.http import HttpResponse
from django.shortcuts import render

#import PDM.MaintenanceLog.MaintenanceLog
from .models import Asset
from django.apps import apps

# Create your views here.
# Take user requests and respond in some kind of way

def index(request):
    return HttpResponse("<h2>hi</h2>")

def newAsset(request):
    FacilityName = request.POST.get('FacilityName', False)
    FactoryNum = request.POST.get('FactoryNum', False)
    Prodline = request.POST.get('Prodline', False)
    MachineID = request.POST.get('MachineID', False)
    Name = request.POST.get('Name', False)
    print(FacilityName)
    asset = Asset(FacilityName=FacilityName, FactoryNum=FactoryNum, Prodline=Prodline, MachineID=MachineID, Name=Name)
    asset.save()
    return HttpResponse(render(request,"assets/NewAsset.html"),{})

def assetDisplay(request):
    assetReg = Asset.objects.all()
    context = {
        'assetReg': assetReg,
    }
    return HttpResponse(render(request, 'assets/AssetDisplay.html', context))

def assetDisplay1(request):
    log = apps.get_model('MaintenanceLog', 'MaintenanceLog')
    assetReg = Asset.objects.all()#
    facilities = Asset.objects.all().distinct()#values("FacilityName").distinct()#filter(Facility="Mumbai")
    factories = Asset.objects.all().distinct()#values("FactoryNum").distinct()#.filter(Facility="Mumbai")
    prodline = Asset.objects.all().distinct()#values("Prodline").distinct()#.filter(Facility="Mumbai")
    machines = Asset.objects.all()#values("MachineID")#.filter(Facility="Mumbai")

    #log = MaintenanceLog.objects.all()
    context = {
        'facilities': facilities,
        'factories': factories,
        'prodline': prodline,
        'machines': machines,
        'assetReg': assetReg,
    }
    return HttpResponse(render(request, 'assets/AssetDisplay1.html', context))

def newAsset1(request):
    return