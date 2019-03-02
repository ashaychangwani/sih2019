from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisplayTable, name='DisplayTable'),
    path('AMCForm/', views.Form, name='Form'),
]