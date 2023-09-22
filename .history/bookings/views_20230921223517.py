from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bookings.models import Booking, Table
from bookings.forms import BookingForm
"""
# Form for updating a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'booking_date', 'booking_time', 'booking_table', 'booking_notes']
"""

class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bookings/booking_add.html'
    form_class = BookingForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(queryset=self.get_queryset())
        return render(request, self.template_name, {'form' : form})

    def form_valid(self, form):
        booking.customer = self.request.user

        party_size = form.cleaned_data []

    def find_free_table(self, party_size, booking_date, booking_time):
        # Retreive all available tables
        available_tables = Table.objects.filter(party_size=party_size, is_available=True)

        for table in available_tables:
            #check availability for specified date and time
            existing_booking = Booking.objects.filter(booking_table=table, booking_date=booking_date, booking_time=booking_time).first()
            if not existing_booking:
                return table
            
        return None

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
            return Booking.objects.filter(customer_name__icontains=names)
        if query:
            return Booking.objects.filter(id=query)
        if dates:
            return Booking.objects.filter(booking_date=dates)
        if self.request.user.is_staff:
            # Bookings today or later
            return Booking.objects.filter(booking_date__gte=date.today())
        else:
            # This customer's bookings today or later
            return Booking.objects.filter(
                customer=self.request.user, booking_date__gte=date.today()
            )

# Apply login_required decorator to restrict access to logged-in users
ListBookingView = login_required(BookingListView.as_view())
