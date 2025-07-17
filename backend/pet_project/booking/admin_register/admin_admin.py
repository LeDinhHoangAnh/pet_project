from django.contrib import admin
from booking.models.admins import Admins

@admin.register(Admins)
class AdminsAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_name', 'admin_email', 'role', 'created_at')
    search_fields = ('admin_name', 'admin_email')
    list_filter = ('role',)
