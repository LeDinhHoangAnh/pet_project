from django.contrib import admin
from booking.models.booking_services import BookingServices

@admin.register(BookingServices)
class BookingServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'service', 'quantity', 'unit_price', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')
    search_fields = ('booking__id', 'service__service_name')
    autocomplete_fields = ('booking', 'service')