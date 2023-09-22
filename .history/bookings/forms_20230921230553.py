from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from bookings.models import Booking, Table

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'num_guests','notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        available_tables = Table.objects.filter(is_available=True)
        self.fields['table'].queryset = available_tables

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get('table')
        date = cleaneddata.get('date')
        time = cleaned.data.get('time')
        num_guests = cleaned.data.get('num_guests')
        
        if table:
            try:
                if table.party_size < num_guests:
                    raise ValidationError("Your booking could not be made, there arent enough seats for that time.")

                # Check if the selected table can accommodate the number of guests
                if table.party_size < num_guests:
                    raise ValidationError('The selected table cannot accommodate this number of guests.')

                conflicting_bookings = Booking.objects.filter(table=table, date=date, time=time)
                if conflicting_bookings.exists():
                    raise ValidationError('The selected table is not available at the selected date and time.')
            except Table.DoesNotExist:
                raise ValidationError('Invalid table selection.')

        return cleaned_data