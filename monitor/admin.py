from django.contrib import admin
from monitor.models import Host, Service


class HostAdmin(admin.ModelAdmin):

    list_display =  ('name','description','ipv4','status')
    search_fields = ['name','description','ipv4','status']
    
    fieldsets = (
    
        (None, {
            'fields': ('name', 'description', 'ipv4', 'services', )
        }),
        
        ('Daemon managed options', {
            'classes': ('collapse',),
            'fields': ('services_info', 'last_check', 'status',)
        }),
    )

admin.site.register(Host, HostAdmin)
admin.site.register(Service)
