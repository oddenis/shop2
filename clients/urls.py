from django.contrib import admin
from django.urls import path, include
from .views import clients


urlpatterns = [
    path('', clients, name='clients'),
]