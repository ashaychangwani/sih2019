import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Spares, Order


def DisplayTable(request):
    spares = Spares.objects.all()
    context = {
        'spares' : spares,
    }
    return HttpResponse(render(request, 'spares/spares.html', context))

def PlaceOrder(request):
    if request.method == 'POST':
        MachineID = request.POST.get('machine', False)
        Customer = request.user.username
        Date = datetime.date.today()
        ComponentName = request.POST.get('component', False)
        Count = float(request.POST.get('count', False))
        Cost = float(request.POST.get('cost', False))
        TotalAmount = Cost*Count
        order = Order(MachineID=MachineID, ComponentName=ComponentName, Date2=Date, Customer=Customer, Count=Count, CostOfPart=Cost, TotalAmount=TotalAmount)
        print(MachineID)
        order.save()

    return HttpResponse(render(request,'spares/spareform.html', {}))

def Invoice(request):
    order = Order.objects.all()
    context = {
        'orders': order,
    }
    return HttpResponse(render(request, 'spares/invoice.html', context))