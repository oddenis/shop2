from django.contrib import admin
from.models import Client



admin.site.register(Client)

# Register your models here.
# class ListAdminClient(admin.ModelAdmin):
#     list_display = ('id','first_name', 'last_name', 'phone', 'email')
#
# admin.site.register(Client, ListAdminClient)