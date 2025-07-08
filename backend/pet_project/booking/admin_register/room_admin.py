from django.contrib import admin
from booking.models.rooms import Rooms

@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_name', 'room_number', 'cinema', 'create_at', 'update_at')  
    search_fields = ('room_name', 'room_number')                                          
    list_filter = ('cinema',)                                                              
    ordering = ('-create_at',)                                                              
    list_per_page = 25      