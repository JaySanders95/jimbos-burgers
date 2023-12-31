from django.contrib import admin
from django.urls import path, include
from home.views import home, menu, CustomSignupView
from bookings.views import BookingCreateView, BookingListView, BookingUpdateView, BookingDeleteView
from allauth.account.views import SignupView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('menu/', menu, name="menu"),
    path('accounts/signup/', CustomSignupView.as_view(), name='custom_signup'),
    path("accounts/", include("allauth.urls")),
    path('bookings/', BookingListView.as_view(), name='my_bookings'),
    path('bookings/add/', BookingCreateView.as_view(), name='booking_add'),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_edit'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_defensive'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)