from django.contrib import admin
from django.urls import path, include
from home.views import home, menu
from bookings.views import BookingCreateView, BookingDeleteView, BookingUpdateView, BookingListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('menu/', menu, name="menu"),
    path("accounts/", include("allauth.urls")),
]
