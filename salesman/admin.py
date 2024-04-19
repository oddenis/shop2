from django.contrib import admin
from .models import Salesman, Dolgnost
# Register your models here.


class ListDolgnost(admin.ModelAdmin):
    list_display = ('id', 'dolgnost')

class ListAdminSalesman(admin.ModelAdmin):
    list_display = ('id', 'name', 'familia', 'tel', 'email', 'date_to_work', 'job_title')


admin.site.register(Dolgnost, ListDolgnost)
admin.site.register(Salesman, ListAdminSalesman)