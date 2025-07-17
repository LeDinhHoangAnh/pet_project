from django.contrib import admin
from booking.models.permissions import Permissions

@admin.register(Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'permission_name', 'permission_description')
    search_fields = ('permission_name',)
