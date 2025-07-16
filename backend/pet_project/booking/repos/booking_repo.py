from booking.models.bookings import Bookings
from booking.models.booking_details import BookingDetails
from booking.models.booking_services import BookingServices
from booking.models.services import Services
from booking.models.seat_status_in_showtime import SeatStatusInShowtime

class BookingRepo:
    @staticmethod
    def create_booking(data):
        return Bookings.objects.create(**data)

    @staticmethod
    def create_booking_detail(booking, seat_id):
        return BookingDetails.objects.create(booking=booking, seat_id=seat_id)

    
    @staticmethod
    def create_booking_service(booking, service):
        try:
            service_obj = Services.objects.get(pk=service['id'])
        except Services.DoesNotExist:
            raise Exception(f"Dịch vụ ID {service['id']} không tồn tại.")

        return BookingServices.objects.create(
            booking=booking,
            service=service_obj,
            quantity=service['quantity'],
            unit_price=service_obj.service_price
        )

    @staticmethod
    def update_seat_status(showtime_id, seat_id):
        return SeatStatusInShowtime.objects.update_or_create(
            showtime_id=showtime_id,
            seat_id=seat_id,
            defaults={'status': 'booked'}
        )

