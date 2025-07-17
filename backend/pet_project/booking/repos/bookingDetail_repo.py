from booking.models.booking_details import BookingDetails
from booking.models.booking_services import  BookingServices
from booking.models.seat_prices import SeatPrices
def get_booking_seat_details(booking):
    return BookingDetails.objects.select_related('seat__seat_type').filter(booking=booking)

def get_booking_services(booking):
    return BookingServices.objects.select_related('service').filter(booking=booking)

def get_seat_price_map(showtime):
    seat_prices = SeatPrices.objects.filter(showtime=showtime)
    return {
        (sp.seat_type.id): sp.price
        for sp in seat_prices
    }
