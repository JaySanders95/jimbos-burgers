from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_size = models.IntegerField()
    availability = models.BooleanField(default=True)
    description = models.Textfield(blank=True, null=True, max_length=200)

    def __str__(self):
        return f"Table{self.table_number}"

        