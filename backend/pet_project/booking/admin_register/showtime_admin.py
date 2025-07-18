from django.contrib import admin
from booking.models.showtimes import Showtimes

@admin.register(Showtimes)
class ShowtimesAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'room', 'start_time','create_at', 'update_at')  
    search_fields = ('movie__title', 'room__room_name')                                           
    list_filter = ('room__cinema', 'start_time')                                                  
    ordering = ('-start_time',)
    list_per_page = 25
    autocomplete_fields = ['movie', 'room']