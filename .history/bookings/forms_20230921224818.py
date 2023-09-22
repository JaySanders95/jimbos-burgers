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
        
        if table_id:
            try:
                table = Table.objects.get(id=table_id)

                # Check if the selected table can accommodate the number of guests
                if table.party_size < num_guests:
                    raise ValidationError('The selected table cannot accommodate this number of guests.')

                # Check if the selected table is available at the selected date and time
                conflicting_bookings = Booking.objects.filter(table=table, date=date, time=time)
                if conflicting_bookings.exists():
                    raise ValidationError('The selected table is not available at the selected date and time.')
            except Table.DoesNotExist:
                raise ValidationError('Invalid table selection.')

        
        return cleaned_data