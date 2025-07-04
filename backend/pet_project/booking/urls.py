from django.urls import path
from booking.views.booking_view import BookingListCreateView, BookingDetailView

urlpatterns = [
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
]
