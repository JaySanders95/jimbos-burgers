from django import forms
from bookings.models import Booking

class BookingForm(forms.ModelForm):
    class Meta