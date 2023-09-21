from django.contrib import admin
from django.urls import path, include
from home.views import home, menu
from bookings.views import BookingCreateView, BookingDeleteView, BookingUpdateView, BookingListView

urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='my_bookings'),
    path('bookings/add/', BookingCreateView.as_view(), name='booking_add'),

]
