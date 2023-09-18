from django.db import models
from django.contrib.auth.models import User


from django.db import models

class TimeSlot(models.Model):
    slot_id = models.PositiveIntegerField(primary_key=True)
    slot_description = models.CharField(max_length=100)

    def __str__(self):
        return self.slot_description

class TableSize(models.Model):
    size_id = models.PositiveIntegerField(primary_key=True)
    size_description = models.CharField(max_length=100)

    def __str__(self):
        return self.size_description

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_size = models.ForeignKey(TableSize, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

    class Meta:
        ordering = ["table_number"]

    def __str__(self):
        return f"Table {self.table_number} - {self.table_size}"

class ReservationStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    CONFIRMED = 'Confirmed', 'Confirmed'
    CANCELLED = 'Cancelled', 'Cancelled'

class RestaurantReservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    customer_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=ReservationStatus.choices,
        default=ReservationStatus.PENDING
    )

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.table} on {self.reservation_date}"

    class Meta:
        ordering = ['reservation_date']