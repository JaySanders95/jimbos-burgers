from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from bookings.models import Booking, Table
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookingForm(forms.ModelForm):
    
    date=forms.DateField(widget=forms.widgets.DateInput(attrs={'type' : 'date'}))

    class Meta:
        model = Booking
        fields = ['date', 'time', 'num_guests','notes']


        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        available_tables = Table.objects.filter(is_available=True)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        num_guests = cleaned_data.get('num_guests')

        table = Table.objects.get(id)
        
        if table:
            try:
                if table.capacity < num_guests:
                    raise ValidationError("Your booking could not be made, there arent enough seats for that time.")

                # Check if the selected table can accommodate the number of guests
                if table.capacity < num_guests:
                    raise ValidationError('The selected table cannot accommodate this number of guests.')

                conflicting_bookings = Booking.objects.filter(table=table, date=date, time=time)
                if conflicting_bookings.exists():
                    raise ValidationError('The selected table is not available at the selected date and time.')
            except Table.DoesNotExist:
                raise ValidationError('Invalid table selection.')

        return cleaned_data