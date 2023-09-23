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

    def save(self, commit=True):
        booking = super().save(commit=False)
        #Auto assigns best table based on requirements and availability
        booking.table = self.find_best_table(booking.num_guests, booking.date, booking.time)

        if commit:
            booking.save()
        return booking
    
    def find_best_table(self, requested_capacity, requested_date, requested_time ):
        #Retrieves available tables
        available_tables = Table.objects.filter(capacity__gte=requested_capacity, is_available=True)

        #Find best table for booking
        best_table = available_tables.annotate(capacity_diff=Min(requested_capacity - F('capacity'))).order_by('capacity_diff').first()

        return best_table if best_table else None