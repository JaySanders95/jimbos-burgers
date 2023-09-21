from django import forms
from django.core.exceptions import ValidationError
from bookings.models import Booking, Table

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'num_guests','notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(is_availability=True)

    def clean(self):
        cleaned_data=super().clean()
        table = cleaned.data.get('table')
        date = cleaned.data.get('date')
        time = cleaned.data.get('time')
        num_guests = cleaned.data.get('num_guests')
        
        # Check if the selected table can accommodate the number of guests
        if table and num_guests:
            if table.party_size < num_guests:
                raise ValidationError('The selected table cannot accommodate this number of guests.')

        # Check if the selected table is available at the selected date and time
        if table and date and time:
            conflicting_bookings = Booking.objects.filter(table=table, date=date, time=time)
            if conflicting_bookings.exists():
                raise ValidationError('The selected table is not available at the selected date and time.')

        return cleaned_data