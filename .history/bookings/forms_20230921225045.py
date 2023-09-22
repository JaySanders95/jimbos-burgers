from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from bookings.models import Booking, Table

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'num_guests','notes']

    