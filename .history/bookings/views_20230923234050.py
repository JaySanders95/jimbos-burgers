from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bookings.models import Booking, Table
from bookings.forms import BookingForm

class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bookings/booking_add.html'
    form_class = BookingForm
    model = Booking

    def form_valid(self, form):
        form.instance.customer = self.request.user

        capacity = form.cleaned_data ['num_guests']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']

        table = self.find_free_table(capacity, date, time)
        

        if table:
            booking = Booking.objects.create(
                table=table,
                date=date,
                time=time,
                customer=self.request.user,
                num_guests = capacity
            )
            booking.save()
            messages.success(self.request, "Booking completed successfully!")
            return redirect('booking_add')
        else:
            messages.error(self.request, "Your booking could not be made, please try a different time.")
            return render(self.request, self.template_name, {'form' : form})

    def find_free_table(self, capacity, date, time):
        booking_num = int(capacity)
        if booking_num % 2 == 1:
            booking_num += 1
        
        capacity = str(booking_num)
        # Retreive all available tables
        available_tables = Table.objects.filter(capacity=capacity, is_available=True)

        for table in available_tables:
            #check availability for specified date and time
            existing_booking = Booking.objects.filter(table=table, date=date, time=time).first()
            if not existing_booking:
                return table
            
        return None
    
    def get_queryset(self):
        return Table.objects.filter(is_available=True)


class BookingListView(LoginRequiredMixin, ListView):
    template_name = 'bookings/my_bookings.html'
    model = Booking
    context_object_name = 'bookings'

    def get_queryset(self):
        #Queryset function for managing booking search
        user = self.request.user

        # If user is staff, shows all bookings