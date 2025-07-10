from django.urls import path
from booking.views.movie_view import AdminMovieListCreate, AdminMovieDetail
from booking.views.showtime_view import ShowtimesByMovie
from booking.views.auth_view import RegisterAPIView, LoginAPIView
from booking.views.role_view import RoleListCreateView, RoleDetailView
from booking.views.permission_view import PermissionListCreateView, PermissionDetailView
from booking.views.admin_view import AdminListCreateView, AdminUpdateDeleteView
from booking.views.movieGenre_view import MovieGenresByMovieAPIView

urlpatterns = [
    path('movies/<int:movie_id>/showtimes/', ShowtimesByMovie.as_view(), name='showtimes-by-movie'),
    # ... các API khác
]

urlpatterns = [
    path('movies/', AdminMovieListCreate.as_view(), name='admin-movie-list-create'),
    path('movies/<int:pk>/', AdminMovieDetail.as_view(), name='admin-movie-detail'),
    path('movies/<int:movie_id>/showtimes/', ShowtimesByMovie.as_view(), name='showtimes-by-movie'),
    path('auth/register/', RegisterAPIView.as_view()),
    path('auth/login/', LoginAPIView.as_view()),
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:role_id>/', RoleDetailView.as_view(), name='role-detail'),
    path('permissions/', PermissionListCreateView.as_view(), name='permission-list-create'),
    path('permissions/<int:permission_id>/', PermissionDetailView.as_view(), name='permission-detail'),
    path('admins/', AdminListCreateView.as_view(), name='admin-list-create'),
    path('admins/<int:admin_id>/', AdminUpdateDeleteView.as_view(), name='admin-update-delete'),
    path('movies/<int:movie_id>/genres/', MovieGenresByMovieAPIView.as_view()),
]



