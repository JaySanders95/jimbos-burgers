from django import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bookings.models import Booking, Table

# Form for updating a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'booking_date', 'booking_time', 'booking_table', 'booking_notes']


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'bookings/booking_add.html'
    form_class = BookingForm
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        print("form is valid")
        #Set customer based on logged in user
        form.instance.customer = self.request.user

        #Assign a table
        if table_id and table_id.isdigit():
            form.instance.booking_table = get_object_or_404(Table, id=table_id)
            print(f"Booking Table: {form.instance.booking_table}")  # Debug message to check the assigned table
        else:
            print("Invalid table ID provided.")
        
        #Save the booking
        return super().form_valid(form)

