from django.contrib import admin
from booking.models.bookings import Bookings

from booking.models.movies import Movies
@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'showtime','total_price', 'booking_status','create_at', 'booking_type','customer_name', 'customer_phone', 'update_at']
