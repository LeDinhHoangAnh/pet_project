from booking.repos.seat_repo import get_seats_by_showtime
from booking.serializers.seat_serializer import SeatSerializer
from booking.repos.seat_repo import get_seats_and_status_by_showtime

def get_seat_list_by_showtime(showtime_id):
    showtime, seats = get_seats_by_showtime(showtime_id)

    if showtime is None:
        return None

    serialized_seats = SeatSerializer(seats, many=True).data
    total = seats.count()  # tính tổng ghế

    return {
        'total_seats': total,
        'seats': serialized_seats
    }

def get_seat_status_list_by_showtime(showtime_id):
    seats, booked_ids = get_seats_and_status_by_showtime(showtime_id)
    if seats is None:
        return None

    result = []
    for seat in seats:
        result.append({
            'id': seat.id,
            'seat_number': seat.seat_number,
            'seat_type_name': seat.seat_type.seat_type_name,
            'status': 'booked' if seat.id in booked_ids else 'available'
        })

    return {
        'total': len(seats),
        'seats': result
    }