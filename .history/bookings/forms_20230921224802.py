from django import forms
from django.core.exceptions import ValidationError
from bookings.models import Booking, Table

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'num_guests','notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        available_tables = Table.objects.filter(is_available=True)
        self.fields['table'].choices = [(table.id, str(table)) for table in available_tables]

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned.data.get('table')
        date = cleaned.data.get('date')
        time = cleaned.data.get('time')
        num_guests = cleaned.data.get('num_guests')
        
        # Check if the selected table can accommodate the number of guests
        
        return cleaned_data