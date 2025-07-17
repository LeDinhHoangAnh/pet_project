from django.contrib import admin
from booking.models.roles import Roles

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'create_at', 'update_at')
    search_fields = ('role_name',)