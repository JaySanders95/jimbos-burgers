from django.db import models
from django.contrib.auth.models import User

TABLE_SIZE = (
    (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"),
    (7, "7"), (8, "8"), (9, "9"), (10, "10"), (11, "11"), (12, "12"),
)

TIME_SLOT = (
    (1, "09:00 - 10:00"), (1, "10:00 - 11:00"), (1, "11:00 - 12:00"), (2, "12:00 - 13:00"), (3, "13:00 - 14:00"),
    (4, "14:00 - 15:00"), (5, "15:00 - 16:00"), (6, "16:00 - 17:00"),    (7, "17:00 - 18:00"),
)


class Table(models.Model):
    """Model for a table."""

    table_number = models.PositiveIntegerField(unique=True)
    party_size = models.PositiveIntegerField(choices=TABLE_SIZE, default=2)
    availability = models.BooleanField(default=True)

    class Meta:
        ordering = ["table_number"]

    def __str__(self):
        return f"Table {self.table_number}"


class Booking(models.Model):
    """Model for bookings."""

    customer = models.ForeignKey(User, related_name="booking_name", on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30, null=False)
    booking_date = models.DateField()
    booking_time = models.IntegerField(choices=TIME_SLOT, default=1)
    booking_table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="table")
    timestamp_booking_made = models.DateTimeField(auto_now=True)
    booking_notes = models.CharField(max_length=1000, null=True)

    class Meta:
        ordering = ["booking_date", "booking_time"]

    def __str__(self):
        return f"Booking {self.pk}"

    def formatted_datetime(self):
        """Returns a formatted date and time for display."""
        return f"{self.booking_date.strftime('%Y-%m-%d')} {TIME_SLOT[self.booking_time - 1][1]}"
