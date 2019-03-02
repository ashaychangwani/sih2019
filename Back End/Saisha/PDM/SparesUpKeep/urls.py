from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisplayTable, name='SparesTable'),
    path('PlaceOrder/', views.PlaceOrder, name='PlaceOrder'),
    path('Invoice/', views.Invoice, name='Invoice'),
]