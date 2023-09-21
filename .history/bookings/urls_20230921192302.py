from django.contrib import admin
from django.urls import path, include
from home.views import home, menu
from bookings.views import BookingCreateView, BookingDeleteView, BookingUpdateView, BookingListView

urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='my_bookings'),
    path('bookings/add/', BookingCreateView.as_view(), name='booking_add'),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),Check URL Configuration:
Ensure that the URL for the form submission ({% url 'booking_add' %}) is correct and corresponds to the BookingCreateView.
]
