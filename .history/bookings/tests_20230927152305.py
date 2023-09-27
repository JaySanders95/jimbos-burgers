from django.test import TestCase
from bookings.models import Booking, Table
from django.contrib.auth.models import User

class TableTests(TestCase):
    
    def setUp(self):
        self.table = Table.objects.create(table_number=1, capacity=4, is_available=True)
