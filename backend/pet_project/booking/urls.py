from django.urls import path
from booking.views.seatPrice_view import SeatPriceView
from booking.views.movie_view import AdminMovieListCreate, AdminMovieDetail
from booking.views.showtime_view import ShowtimesByMovie, ShowtimeDetailAPIView
from booking.views.auth_view import RegisterAPIView, LoginAPIView
from booking.views.role_view import RoleListCreateView, RoleDetailView
from booking.views.permission_view import PermissionListCreateView, PermissionDetailView
from booking.views.admin_view import AdminListCreateView, AdminUpdateDeleteView
from booking.views.movieGenre_view import MovieGenresByMovieAPIView
from booking.views.seat_view import SeatByShowtimeView
from booking.views.seat_view import SeatStatusShowtimeView
from booking.views.service_view import ServiceListView
from booking.views.userProfile_view import UserProfileView
from booking.views.booking_view import BookingCreateView
from booking.views.bookingHistory_view import BookingHistoryView

urlpatterns = [
    path('movies/<int:movie_id>/showtimes/', ShowtimesByMovie.as_view(), name='showtimes-by-movie'),
    # ... các API khác
]

urlpatterns = [
    path('movies/', AdminMovieListCreate.as_view(), name='admin-movie-list-create'),
    path('movies/<int:pk>/', AdminMovieDetail.as_view(), name='admin-movie-detail'),
    path('movies/<int:movie_id>/showtimes/', ShowtimesByMovie.as_view(), name='showtimes-by-movie'),
    path('auth/register/', RegisterAPIView.as_view()),
    path('auth/login1/', LoginAPIView.as_view()),
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:role_id>/', RoleDetailView.as_view(), name='role-detail'),
    path('permissions/', PermissionListCreateView.as_view(), name='permission-list-create'),
    path('permissions/<int:permission_id>/', PermissionDetailView.as_view(), name='permission-detail'),
    path('admins/', AdminListCreateView.as_view(), name='admin-list-create'),
    path('admins/<int:admin_id>/', AdminUpdateDeleteView.as_view(), name='admin-update-delete'),
    path('movies/<int:movie_id>/genres/', MovieGenresByMovieAPIView.as_view()),
    path('showtimes/<int:showtime_id>/seats/', SeatByShowtimeView.as_view(), name='seats-by-showtime'),
    path('showtimes/<int:showtime_id>/seat_status/', SeatStatusShowtimeView.as_view(), name='seats-status-by-showtime'),
    path('seat-prices/<int:showtime_id>/', SeatPriceView.as_view(), name='get_seat_prices'),
    path('showtimes/<int:showtime_id>/detail/', ShowtimeDetailAPIView.as_view(),name='showtime-detail'),
    path('services/', ServiceListView.as_view(), name='get-all-services'),
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('bookings/', BookingCreateView.as_view(), name='create-booking'),
    path('booking/history/', BookingHistoryView.as_view(), name='booking-history'),
]




