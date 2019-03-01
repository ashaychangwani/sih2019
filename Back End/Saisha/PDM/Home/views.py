from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h2>this is the home page</h2>")#render(request,'home.html',{}))