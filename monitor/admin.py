from django.contrib import admin
from .models import Host, Port, Log


class PortInLines (admin.TabularInline):
    model = Port
    extra = 1

class LogInLines (admin.TabularInline):
    model = Log
    extra = 0

class HostAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name', 'description', 'ipv4']}),
#        ('Daemon Managed Status', {'fields': ['last_check', 'last_status_change', 'status_info'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'description', 'ipv4', 'status')
    search_fields = ['name', 'description', 'ipv4', 'status']
    inlines = [PortInLines]

admin.site.register(Host, HostAdmin)
