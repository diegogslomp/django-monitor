from django.contrib import admin
from .models import Host, Port


class PortInLines (admin.TabularInline):
    model = Port
    extra = 1

class HostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'ipv4']}),
        ('Daemon Managed Status', {'fields': ['status', 'status_info', 'last_status_change', 'last_check'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'description', 'ipv4', 'status')
    search_fields = ['name', 'description', 'ipv4', 'status']
    inlines = [PortInLines]

admin.site.register(Host, HostAdmin)
