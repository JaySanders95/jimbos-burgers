from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bookings.models import Booking, Table
"""
# Form for updating a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'booking_date', 'booking_time', 'booking_table', 'booking_notes']
"""

class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bookings/booking_add.html'

    def get(self, request):
        form = BookingForm()
        return render(request, self.template_name, {'form' : form})

        if form.is_valid():
            #Save booking
            booking = form.save(commit=False)
            booking.customer = request.user
            
            #Find free table based on requirements
            table = self.find_free_table(booking.party_size_for_booking, booking.booking_date, booking.booking_time)

            if table:
                booking.booking_table = table
                booking.save()
                messages.success(request, "Booking completed successfully!")
                return redirect('my_bookings')
            else:
                messages.error(request, 'No free tables available for the selected party size and time.')
                return render(request, self.template_name, {'form': form})
        else:
            #Invalid form, reload page with errors
            return render(request, self.tempalte_name, {'form':form})

        def find_free_table(self, party_size, booking_date, booking_time):
            # Retreive all available tables
            available_tables = Table.objects.filter(party_size=party_size, availability=True)

            for table in available_tables:
                #check availability for specified date and time
                