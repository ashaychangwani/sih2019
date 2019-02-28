from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Spares

def DisplayTable(request):
    spares = Spares.objects.all()
    context = {
        'spares' : spares,
    }
    return HttpResponse(render(request, 'spares.html', context))