from django.contrib import admin
from django.urls import path, include
from .views import salesman


urlpatterns = [
    path('', salesman, name='salesman'),
]