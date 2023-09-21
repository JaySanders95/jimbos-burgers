from django.db import models
from django.contrib.auth.models import User

TABLE_SIZE = (
    (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"),
    (7, "7"), (8, "8"), (9, "9"), (10, "10"), (11, "11"), (12, "12"),
)

TIME_SLOT = (
    (1, "09:00 - 10:00"), (2, "10:00 - 11:00"), (3, "11:00 - 12:00"), (4, "12:00 - 13:00"), (5, "13:00 - 14:00"),
    (6, "14:00 - 15:00"), (7, "15:00 - 16:00"), (8, "16:00 - 17:00"), (9, "17:00 - 18:00"),
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


