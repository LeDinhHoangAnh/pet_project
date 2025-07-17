from django.contrib import admin
from booking.models.bookings import Bookings

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = (
        'id','showtime', 'total_price', 'booking_status',
        'booking_type', 'admin', 'customer_name', 'customer_phone',
        'create_at', 'update_at'
    )
    list_filter = ('booking_status', 'booking_type', 'create_at', 'update_at')
    search_fields = ('id', 'customer_name', 'customer_phone', 'user__user_email')
    autocomplete_fields = ('admin', 'showtime') 