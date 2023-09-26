from django.test import TestCase
from bookings.models import Booking, Table
from django.contrib.auth.models import User

class TableTests(TestCase):
    def test_table_str(self):
        table = Table(table_number, capacity = 4)
        self.assertEqual(str(table), 'Table1')
