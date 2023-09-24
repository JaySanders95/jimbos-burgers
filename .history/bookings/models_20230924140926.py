from django.db import models
from django.contrib.auth.models import User

#
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
    notes = models.TextField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_time_display(self):
        """Get the display value of the selected time."""
        time_choices_display = dict(TIME_CHOICES)
        return time_choices_display.get(self.time, 'Unknown')

    def __str__(self):
        return f" Covers: {self.num_guests} Date: {self.date}"
