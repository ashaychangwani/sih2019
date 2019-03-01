from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import AMC

def DisplayTable(request):
    amc = AMC.objects.all()
    context = {
        'amc': amc,
    }
    return HttpResponse(render(request, 'amc.html', context))