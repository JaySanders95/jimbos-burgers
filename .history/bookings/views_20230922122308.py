from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bookings.models import Booking, Table

https://8000-jaysanders9-jimbosburge-8h9yxt8i8os.ws-eu104.gitpod.io/
class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bookings/booking_add.html'
    form_class = BookingForm
    model = Booking

    def form_valid(self, form):
        booking.customer = self.request.user

        party_size = form.cleaned_data ['num_guests']
        booking_date = form.cleaned_data['date']
        booking_time = form.cleaned_data['time']

        table = self.find_free_table(party_size, booking_date, booking_time)

        if table:
            booking.table = table
            booking.save()
            messages.success(self.request, "Booking completed successfully!")
            return redirect('my_bookings')
        else:
            messages.error(self.request, "Your booking could not be made, please try a different time.")
            return render(self.request, self.template_name, {'form' : form})

    def find_free_table(self, party_size, booking_date, booking_time):
        # Retreive all available tables
        available_tables = Table.objects.filter(party_size=party_size, is_available=True)

        for table in available_tables:
            #check availability for specified date and time
            existing_booking = Booking.objects.filter(booking_table=table, booking_date=booking_date, booking_time=booking_time).first()
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
