from django.db import models
from django.contrib.auth.models import User

Tfrom django.db import models

class TimeSlots(models.IntegerChoices):
    SLOT_9AM = 1, '9:00 AM - 10:00 AM'
    SLOT_9AM = 1, '10:00 AM - 11:00 AM'
    SLOT_9AM = 1, '11:00 AM - 12:00 PM'
    SLOT_9AM = 1, '12:00 PM - 1:00 PM'
    SLOT_9AM = 1, '1:00 PM - 2:00 PM'
    SLOT_9AM = 1, '3:00 AM - 15:00 AM'
    SLOT_12PM = 2, '15:00 PM - 16:00 PM'
    SLOT_3PM = 3, ':00 PM - 4:00 PM'
    # Add more time slots as needed

class TableSizes(models.IntegerChoices):
    SMALL = 1, 'Small (2-4 seats)'
    MEDIUM = 2, 'Medium (4-6 seats)'
    LARGE = 3, 'Large (6+ seats)'

class ReservationStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    CONFIRMED = 'Confirmed', 'Confirmed'
    CANCELLED = 'Cancelled', 'Cancelled'

class RestaurantReservation(models.Model):
    table_number = models.IntegerField()
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