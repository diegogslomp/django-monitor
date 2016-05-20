from django.contrib import admin
from .models import Host


class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'ipv4', 'status')
    search_fields = ['name', 'description', 'ipv4', 'status']

admin.site.register(Host, HostAdmin)
