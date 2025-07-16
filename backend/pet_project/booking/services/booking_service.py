from booking.repos.booking_repo import BookingRepo
from django.utils import timezone

class BookingService:
    @staticmethod
    def create_booking(user, validated_data):
        booking_data = {
            'user': user,
            'showtime_id': validated_data['showtime_id'],
            'total_price': validated_data['total_price'],
            'booking_status': 'confirmed',
            'booking_type': 'online',
            'customer_name': user.user_name,
            'customer_phone': user.user_phone,
            'create_at': timezone.now()
        }

        booking = BookingRepo.create_booking(booking_data)

        for seat_id in validated_data['seat_ids']:
            BookingRepo.create_booking_detail(booking, seat_id)
            BookingRepo.update_seat_status(validated_data['showtime_id'], seat_id)

        for service in validated_data['services']:
            BookingRepo.create_booking_service(booking, service)

        return booking

