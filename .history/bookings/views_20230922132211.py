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
            booking.table = table
            booking.table.save()
            messages.success(self.request, "Booking completed successfully!")
            return redirect('my_bookings')
        else:
            messages.error(self.request, "Your booking could not be made, please try a different time.")
            return render(self.request, self.template_name, {'form' : form})

    def find_free_table(self, capacity, date, time):
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
    template_name = 'bookings/booking_add.html'
    model = Booking
    context_object_name = 'bookings'

    def get_queryset(self):
        """Queryset function for managing booking search"""
        query = self.request.GET.get("ref")
        dates = self.request.GET.get("date")
        names = self.request.GET.get("name")
        if names:
            return Booking.objects.filter(name__icontains=names)
        if query:
            return Booking.objects.filter(id=query)
        if dates:
            return Booking.objects.filter(date=dates)
        if self.request.user.is_staff:
            # Bookings today or later
            return Booking.objects.filter(date__gte=date.today())
        else:
            # This customer's bookings today or later
            return Booking.objects.filter(
                customer=self.request.user, date__gte=date.today()
            )

# Apply login_required decorator to restrict access to logged-in users
ListBookingView = login_required(BookingListView.as_view())
