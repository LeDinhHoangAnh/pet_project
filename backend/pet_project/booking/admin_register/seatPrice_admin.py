from django.contrib import admin
from booking.models.seat_prices import SeatPrices  # hoặc đúng path tới model

@admin.register(SeatPrices)
class SeatPricesAdmin(admin.ModelAdmin):
    list_display = ('id', 'showtime', 'seat_type', 'price', 'create_at', 'update_at')
    search_fields = ('seat_type__seat_type_name', 'showtime__movie__title')
    list_filter = ('seat_type', 'showtime')
    ordering = ('-create_at',)
    list_per_page = 25

    # Tùy chọn nếu bạn muốn ẩn các trường thời gian dưới collapse
    fieldsets = (
        (None, {
            'fields': ('showtime', 'seat_type', 'price')
        }),
        ('Thông tin hệ thống', {
            'fields': ('create_at', 'update_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('create_at', 'update_at')
