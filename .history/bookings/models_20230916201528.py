from django.db import models
from django.contrib.auth.models import User

TABLE_SIZE = ((1, "1"),(2, "2"),(3, "3"),(4, "4"),(5, "5"),(6, "6"),(7, "7"),(8, "8"),(9, "9"),(10, "10"),(11, "11"),(12, "12"),)

TIME_SLOT = (
    (1, "11:00 - 12:00"),
    (2, "12:00 - 13:00"),
    (3, "13:00 - 14:00"),
    (4, "14:00 - 15:00"),
    (5, "15:00 - 16:00"),
    (6, "16:00 - 17:00"),
    (7, "17:00 - 18:00"),
    (8, "18:00 - 19:00"),
    (9, "19:00 - 20:00"),
    (10, "20:00 - 21:00"),
    (11, "21:00 - 22:00"),
)

class Table(models.Model):
    """ Model for table """
    table_number = models.PositiveIntegerField(unique=True)
    table_num_seats = models.PositiveIntegerField(choices=TABLE_SIZE, default=2)
    