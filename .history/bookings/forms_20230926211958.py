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
        widgets = {
            'num_guests': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        booking = super().save(commit=False)
        #Auto assigns best table based on requirements and availability
        booking.table = self.find_best_table(booking.num_guests, booking.date, booking.time)
        
<script>
    document.getElementById('id_date').placeholder = '{{ form.instance.date}}';
    document.getElementById('id_time').placeholder = '{{ form.instance.get_time_display}}';
    document.getElementById('id_num_guests').placeholder = '{{ form.instance.num_guests}}';
    document.getElementById('id_table').placeholder = '{{ form.instance.table}}';
    document.getElementById('id_notes').placeholder = '{{ form.instance.notes}}';

  
    // JavaScript to prevent selecting a past date
    const dateInput = document.getElementById("{{ form.date.auto_id }}");
    dateInput.addEventListener('change', function() {
        const today = new Date().toISOString().split('T')[0];
        if (dateInput.value < today) {
            dateInput.value = today;
        }
    });

    // JavaScript to prevent selecting a past time
    const timeInput = document.getElementById("{{ form.time.auto_id }}");
    timeInput.addEventListener('change', function() {
        const now = new Date();
        const selectedTime = new Date(`2000-01-01T${timeInput.value}`);
        if (selectedTime < now) {
            const hours = now.getHours().toString().padStart(2, '0');
            const minutes = now.getMinutes().toString().padStart(2, '0');
            timeInput.value = `${hours}:${minutes}`;
        }
    });

</script> 

i want to put all of this in a script.js file. how would i call it for :

{% extends 'base.html' %}
{% load static %}
{% load crispy_forms_tags %}

{% block content %}

<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6 text-center bg-light border border-lg">
            <h2 class="mt5 mb-4"> Edit Booking</h2>
            <form method="post" class="mt-5">
                {% csrf_token %}
                <div class="form-group">
                    <label for="{{ form.date.id_for_label }}">Date:</label>
                    {{ form.date }}
                </div><br>

                <div class="form-group">
                    <label for="{{ form.time.id_for_label }}">Time:</label>
                    {{ form.time }}
                </div><br>

                <div class="form-group">
                    <label for="{{ form.num.guests.id_for_label }}">Number of Guests:</label>
                    {{ form.num_guests }}
                </div><br>

                <div class="form-group">
                    <label for="{{ form.notes.id_for_label }}">Notes:</label>
                    {{ form.notes }}
                </div><br>

                <input type="submit" value="Submit">
            </form>
        </div>
    </div>
</div>
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
        