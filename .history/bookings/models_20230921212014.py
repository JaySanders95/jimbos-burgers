from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Table (models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table{self.table_number}"

class Booking(models.Model):

    TIME_CHOICES = [
        (1, "09:00 - 10:00"), (2, "10:00 - 11:00"), (3, "11:00 - 12:00"), 
        (4, "12:00 - 13:00"), (5, "13:00 - 14:00"),(6, "14:00 - 15:00"), 
        (7, "15:00 - 16:00"), (8, "16:00 - 17:00"), (9, "17:00 - 18:00")

    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField()
    num_guests = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return f"Booking for {self.customer.username} at {self.date}{self.time}"