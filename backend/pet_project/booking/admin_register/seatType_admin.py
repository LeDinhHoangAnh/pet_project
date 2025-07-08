from django.contrib import admin
from booking.models.seat_types import SeatTypes  # hoặc đường dẫn đúng tới model

@admin.register(SeatTypes)
class SeatTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'seat_type_name', 'seat_type_status', 'seat_type_color_code', 'create_at', 'update_at')
    search_fields = ('seat_type_name', 'seat_type_status')
    list_filter = ('seat_type_status',)
    ordering = ('-create_at',)
    list_per_page = 25
