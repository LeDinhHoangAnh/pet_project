from django.contrib import admin
from booking.models.seat_status_in_showtime import SeatStatusInShowtime

@admin.register(SeatStatusInShowtime)
class SeatStatusInShowtimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'showtime', 'seat', 'status')
    list_filter = ('status', 'showtime')
    search_fields = ('seat__id', 'seat__seat_row', 'seat__seat_column', 'showtime__id')
