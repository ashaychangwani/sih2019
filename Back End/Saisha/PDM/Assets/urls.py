from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('NewAsset/', views.newAsset, name='NewAsset'),
    path('AssetDisplay/', views.assetDisplay, name='assetDisplay'),
]

