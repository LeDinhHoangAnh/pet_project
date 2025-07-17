from django.contrib import admin
from booking.models.role_permissions import RolePermissions

@admin.register(RolePermissions)
class RolePermissionsAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')
    search_fields = ('role__role_name', 'permission__permission_name')