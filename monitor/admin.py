from django.contrib import admin
from .models import Log, Host


class LogInLines (admin.TabularInline):
    model = Log

class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'ipv4', 'status')
    search_fields = ['name', 'description', 'ipv4', 'status']
    inlines = [LogInLines]

admin.site.register(Host, HostAdmin)
