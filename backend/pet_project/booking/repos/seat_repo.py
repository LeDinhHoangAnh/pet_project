from booking.models.showtimes import Showtimes
from booking.models.seats import Seats
from booking.models.seat_status_in_showtime import SeatStatusInShowtime

def get_seats_by_showtime(showtime_id):
    # B1: lấy suất chiếu, kèm phòng
    showtime = (
        Showtimes.objects
        .select_related('room')
        .get(id=showtime_id)
    )

    # B2: lấy danh sách ghế trong phòng chiếu đó, kèm loại ghế
    seats = (
        Seats.objects
        .filter(room=showtime.room)
        .select_related('seat_type')  # nối bảng seat_type để hiển thị tên
        .order_by('seat_number')      # sắp xếp để dễ xử lý frontend
    )

    return showtime, seats

def get_seats_and_status_by_showtime(showtime_id):
    try:
        showtime = Showtimes.objects.select_related('room').get(id=showtime_id)
    except Showtimes.DoesNotExist:
        return None, None

    seats = Seats.objects.filter(room=showtime.room).select_related('seat_type')
    booked_seats = SeatStatusInShowtime.objects.filter(showtime=showtime)
    booked_seat_ids = set(b.seat_id for b in booked_seats)

    return seats, booked_seat_ids