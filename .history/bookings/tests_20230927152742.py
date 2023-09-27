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
        #TEst table fields
        self.assertEqual(self.table.table_number, 1)
        self.assertEqual(self.table.capacity, 4)
        self.assertEqual(self.table.is_available)

    def test_table_unique_constraint(self):
        #Test unique constraint on table_number
        with self.assertRaises(Exception):
            Table.objects.create(table)
        
