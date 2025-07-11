from booking.models.seat_prices import SeatPrices

def get_prices_for_showtime(showtime_id):
    return SeatPrices.objects.filter(showtime_id=showtime_id)
