from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisplayWorkOrders, name='DisplayWorkOrders'),
    path('WOForm/', views.WorkOrderForm, name='WorkOrderForm'),
]