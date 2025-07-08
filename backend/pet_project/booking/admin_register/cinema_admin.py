from django.contrib import admin
from booking.models.cinemas import Cinemas

@admin.register(Cinemas)
class CinemasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cinemas_name', 'cinemas_address', 'create_at', 'update_at')  
    search_fields = ('cinemas_name', 'cinemas_address')                                 
    list_filter = ('create_at',)                                                         
    ordering = ('-create_at',)                                                          
    list_per_page = 25       