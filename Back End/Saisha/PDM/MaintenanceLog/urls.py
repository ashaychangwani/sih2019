from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('MaintenanceLog', views.maintenanceLog, name='maintenanceLog'),
    path('PendingLog', views.pendingLog, name='PendingLog'),
]