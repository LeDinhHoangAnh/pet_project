# pet_project/urls.py
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Welcome to Movie Booking API!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),       # <-- sửa lại dòng này
    path('api/', include('booking.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
