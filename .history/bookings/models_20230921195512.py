from django.db import models
from django.contrib.auth.models import User

class Table (models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table{self.table_number}"

class Booking(models.Model):
    customer = models.ForeignKey