from .admin_register.cinema_admin import *
from .admin_register.movie_admin import *
from .admin_register.room_admin import *
from .admin_register.seat_admin import *
from .admin_register.seatType_admin import *
from .admin_register.showtime_admin import *
from .admin_register.seatPrice_admin import *
from .admin_register.genre_admin import *
from .admin_register.movieGenre_admin import *

from django.contrib import admin
from booking.models.admins import Admins
from booking.models.roles import Roles
from booking.models.permissions import Permissions
from booking.models.role_permissions import RolePermissions
from booking.models.users import Users
@admin.register(Admins)
class AdminsAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_name', 'admin_email', 'role', 'created_at')
    search_fields = ('admin_name', 'admin_email')
    list_filter = ('role',)

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'create_at', 'update_at')
    search_fields = ('role_name',)

@admin.register(Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'permission_name', 'permission_description')
    search_fields = ('permission_name',)

@admin.register(RolePermissions)
class RolePermissionsAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')
    search_fields = ('role__role_name', 'permission__permission_name')
admin.site.register(Users)