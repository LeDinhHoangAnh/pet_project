from booking.repos.bookingDetail_repo import (
    get_booking_seat_details,
    get_booking_services,
    get_seat_price_map
)

def get_booking_detail_info(booking):
    seat_details = []
    total_seat_price = 0

    seat_price_map = get_seat_price_map(booking.showtime)
    booking_seats = get_booking_seat_details(booking)

    for bd in booking_seats:
        seat = bd.seat
        seat_type = seat.seat_type
        price = seat_price_map.get(seat_type.id, 0)
        seat_details.append({
            "seat_number": seat.seat_number,
            "seat_type": seat_type.seat_type_name,
            "price": price,
        })
        total_seat_price += price

    services = []
    total_service_price = 0
    booking_services = get_booking_services(booking)

    for bs in booking_services:
        total_price = bs.quantity * bs.unit_price
        services.append({
            "service_name": bs.service.service_name,
            "quantity": bs.quantity,
            "unit_price": bs.unit_price,
            "total_price": total_price,
        })
        total_service_price += total_price

    return {
        "seats": seat_details,
        "total_seat_price": total_seat_price,
        "services": services,
        "total_service_price": total_service_price,
        "total_price": total_seat_price + total_service_price,
    }
