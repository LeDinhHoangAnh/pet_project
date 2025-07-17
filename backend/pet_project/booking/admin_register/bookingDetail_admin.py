from django.contrib import admin
from booking.models.booking_details import BookingDetails

@admin.register(BookingDetails)
class BookingDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'seat', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')
    search_fields = ('booking__id', 'seat__id')
    autocomplete_fields = ('booking', 'seat')