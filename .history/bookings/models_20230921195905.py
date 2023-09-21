from django.db import models
from django.contrib.auth.models import User

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
    time = models.Timefield()
    num_guests = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return f"Booking for {self.customer}"