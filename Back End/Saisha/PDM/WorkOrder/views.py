from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import WorkOrder


def DisplayWorkOrders(request):
    wo = WorkOrder.objects.all()
    context = {
        'wo': wo,
    }
    return HttpResponse(render(request, 'wo.html', context))