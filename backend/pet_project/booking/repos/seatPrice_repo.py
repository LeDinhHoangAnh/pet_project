from booking.models.seat_prices import SeatPrices

class SeatPricesRepo:
    @staticmethod
    def get_seat_prices_by_showtime(showtime_id):
        return SeatPrices.objects.filter(showtime_id=showtime_id)
