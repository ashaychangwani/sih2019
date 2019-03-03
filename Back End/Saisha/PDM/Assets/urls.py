from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('NewAsset/', views.newAsset1, name='NewAsset'),
    path('AssetDisplay/', views.assetDisplay1, name='assetDisplay'),
]

