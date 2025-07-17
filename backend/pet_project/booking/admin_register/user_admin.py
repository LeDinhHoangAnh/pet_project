from django.contrib import admin
from booking.models.users import Users
from booking.models.roles import Roles

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user_email', 'user_phone', 'role', 'created_at')
    list_filter = ('role', 'account_type',)
    search_fields = ('user_name', 'user_email', 'user_phone')
    readonly_fields = ('created_at', 'create_at', 'update_at')

    fieldsets = (
        (None, {
            'fields': ('user_name', 'user_email', 'user_phone', 'user_address', 'password_hash', 'role', 'account_type')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'create_at', 'update_at')
        }),
    )
