
from __future__ import unicode_literals
from django.contrib.auth.models import User
from background_task import background

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse

# Create your views here.

from .tasks import SchedulingAlgo

def SchedulingView(request):
    print("hi")
    SchedulingAlgo(0,schedule=1,repeat=1)
    print("hello")
    return redirect("Home/")