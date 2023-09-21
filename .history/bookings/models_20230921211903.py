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

    TIME_CHOICES

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(default=timezone.now)
    num_guests = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return f"Booking for {self.customer.username} at {self.date}{self.time}"