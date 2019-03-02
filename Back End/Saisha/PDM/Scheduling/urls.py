from django.http import JsonResponse
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SchedulingView, name="Scheduling"),
]