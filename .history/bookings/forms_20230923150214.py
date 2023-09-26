from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from bookings.models import Booking, Table
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db.models import Q

class BookingForm(forms.ModelForm):
    #Max table size is 12
    NUM_GUESTS_CHOICES = [(i, str(i)) for i in range(1,13)]
    num_guests = forms.ChoiceField(choices=NUM_GUESTS_CHOICES, label= 'Number of guests')


    #Date-selector for 'date'
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
    
    def find_best_table(self, requested_capacity, requested_date, requested_time):
        
        extra_capacity = 1 if requested_capacity % 2 == 1 else 0
        
        #Retrieves available tables
        available_tables = Table.objects.filter(
        Q(capacity__gte=requested_capacity) |
        Q(capacity__gte=requested_capacity + extra_capacity, capacity__in=[2,3,4,5,6,10,12]) 
        ).filter(is_available=True)

        #Find best table for booking
        best_table = None
        min_capacity_diff = float('inf')

        for table in available_tables:
            capacity_diff = table.capacity - requested_capacity
            if 0 <= capacity_diff <= 2 and capacity_diff < min_capacity_diff:
                best_table = table
                min_capacity_diff = capacity_diff
            
        return best_table
        