from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_size = models.IntegerField()
    availability = models.BooleanField