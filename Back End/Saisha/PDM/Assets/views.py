from django.http import HttpResponse
from django.shortcuts import render
from .models import Asset

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
