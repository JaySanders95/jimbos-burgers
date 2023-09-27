from django.test import TestCase
from bookings.models import Booking, Table
from django.contrib.auth.models import User
from datetime import date

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
        self.assertEqual(self.table.is_available, True)

    def test_table_unique_constraint(self):
        #Test unique constraint on table_number
        with self.assertRaises(Exception):
            Table.objects.create(table_number=1, capacity=2, is_available=True)
        
class BookingTest(TestCase):
    
    def setUp(self):
        #Creates a user, table and booking for table
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.table = Table.objects.create(table_number=1, capacity=4, is_available=True)
        self.booking = Booking.objects.create(
            customer=self.user,
            table=self.table,
            date=date(2023, 11, 12),
            time= 3,
            num_guests=3,
            notes="Notes"
        )

    def test_booking_str_representation(self):
        
        expected_str = "Covers: 3 Date: 2023-10-15"
        self.assertEqual(str(self.booking), expected_str)

