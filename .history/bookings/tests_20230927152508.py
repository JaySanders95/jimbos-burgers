from django.test import TestCase
from bookings.models import Booking, Table
from django.contrib.auth.models import User

class TableTests(TestCase):
    
    def setUp(self):
        #Creates a table for testing
        self.table = Table.objects.create(table_number=1, capacity=4, is_available=True)

    def test_table_str_representation(self):
        #Test string representation
        self.assertEqual(str(self.table), "Table1")
    
    def test_table_fields(self):
        
