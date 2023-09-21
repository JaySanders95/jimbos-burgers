from django.contrib import admin
from bookings.models import Table, Booking

admin.register(Table)


admin.site.register(Booking)