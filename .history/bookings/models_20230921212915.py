from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

TIME_CHOICES = (
        (1, "09:00"), (2, "10:00"), (3, "11:00"), 
        (4, "12:00"), (5, "13:00"),(6, "14:00"), 
        (7, "15"), (8, "16:00"), (9, "17:00")
)

class Table (models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table{self.table_number}"

class Booking(models.Model):



    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField(choices=TIME_CHOICES, default=1)
    num_guests = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_time_display(self):
        """Get the display value of the selected time."""
        return dict(self.TIME_CHOICES).get(self.time, 'Unknown')

    def __self__(self):
        return f"Booking for {self.customer.username} at {self.date}{self.time}"