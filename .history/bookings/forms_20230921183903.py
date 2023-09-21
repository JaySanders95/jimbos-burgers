from django import forms
from bookings.models import Booking, Table, TIME_SLOT 

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'booking_date', 'booking_time', 'booking_notes']

        # Add labels for the fields
        labels = {
            'customer_name': 'Customer Name',
            'booking_date': 'Booking Date',
            'booking_time': 'Booking Time',
            'booking_notes': 'Booking Notes'
            ''
        }

        # Datepicker widget for booking_date
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'})
        }

        # Define error messages for required fields
        error_messages = {
            'customer_name': {
                'required': 'Customer name is required.'
            },
            'booking_date': {
                'required': 'Booking date is required.'
            },
            'booking_time': {
                'required': 'Booking time is required.'
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the party_size from the form data
        party_size = self.data.get('party_size')

        # Filter TIME_SLOT based on party_size
        if party_size:
            available_time_slots = [(key, value) for key, value in TIME_SLOT if key <= party_size]
        else:
            available_time_slots = TIME_SLOT

        # Update the choices for booking_time field
        self.fields['booking_time'].choices = available_time_slots

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data