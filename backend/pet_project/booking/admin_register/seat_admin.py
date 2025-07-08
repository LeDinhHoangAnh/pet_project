from django.contrib import admin, messages
from django.urls import path
from booking.models.rooms import Rooms
from django import forms
from booking.models.seat_types import SeatTypes
from booking.models.seats import Seats
from django.template.response import TemplateResponse
from django.shortcuts import redirect

class BulkAddSeatsForm(forms.Form):
    room = forms.ModelChoiceField(queryset=Rooms.objects.all())
    seat_type = forms.ModelChoiceField(queryset=SeatTypes.objects.all())
    quantity = forms.IntegerField(min_value=1, max_value=100)
    prefix = forms.CharField(initial="A", max_length=2)

@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'seat_number', 'seat_type', 'room')
    list_filter = ('room', 'seat_type')
    search_fields = ('seat_number',)
    actions = ['bulk_add_seats']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('bulk-add/', self.admin_site.admin_view(self.bulk_add_seats_view), name='bulk-add-seats')
        ]
        return custom_urls + urls

    def bulk_add_seats(self, request, queryset):
        return redirect('admin:bulk-add-seats')  # Điều hướng tới form

    bulk_add_seats.short_description = "➕ Thêm nhiều ghế một lần"

    def bulk_add_seats_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
        )

        if request.method == 'POST':
            form = BulkAddSeatsForm(request.POST)
            if form.is_valid():
                room = form.cleaned_data['room']
                seat_type = form.cleaned_data['seat_type']
                quantity = form.cleaned_data['quantity']
                prefix = form.cleaned_data['prefix']

                last_index = Seats.objects.filter(room=room, seat_number__startswith=prefix).count()
                new_seats = []

                for i in range(1, quantity + 1):
                    seat_number = f"{prefix}{last_index + i}"
                    new_seats.append(Seats(seat_number=seat_number, seat_type=seat_type, room=room))

                Seats.objects.bulk_create(new_seats)
                self.message_user(request, f"Đã thêm {quantity} ghế mới vào phòng {room.room_name}", messages.SUCCESS)
                return redirect('..')
        else:
            form = BulkAddSeatsForm()

        context['form'] = form
        return TemplateResponse(request, "admin/bulk_add_seats.html", context)

