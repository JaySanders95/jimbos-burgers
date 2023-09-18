from django.db import models
from django.contrib.auth.models import User


class TimeSlots(models.IntegerChoices):
    SLOT_1 = 1, '9:00 AM - 10:00 AM'
    SLOT_2 = 1, '10:00 AM - 11:00 AM'
    SLOT_3 = 1, '11:00 AM - 12:00 PM'
    SLOT_4 = 1, '12:00 PM - 1:00 PM'
    SLOT_5 = 1, '1:00 PM - 2:00 PM'
    SLOT_6 = 1, '3:00 PM - 4:00 PM'
    SLOT_7 = 2, '4:00 PM - 5:00 PM'

class TableSizes(models.IntegerChoices):
    SMALL = 1, 'Small (2-4 seats)'
    MEDIUM = 2, 'Medium (4-6 seats)'
    LARGE = 3, 'Large (6+ seats)'

class ReservationStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    CONFIRMED = 'Confirmed', 'Confirmed'
    CANCELLED = 'Cancelled', 'Cancelled'

class RestaurantReservation(models.Model):
    table_number = models.IntegerField(unique=True)
    table_size = models.PositiveIntegerField(choices=TableSizes.choices)
    time_slot = models.PositiveIntegerField(choices=TimeSlots.choices)
    reservation_date = models.DateField()
    customer_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=ReservationStatus.choices,
        default=ReservationStatus.PENDING
    )

    def __str__(self):
        return f"Reservation for {self.customer_name} at {TimeSlots(self.time_slot).label} on {self.reservation_date}"

    class Meta:
        ordering = ['reservation_date', 'time_slot']