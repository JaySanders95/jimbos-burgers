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

    def get(self, request)
    form = BookingForm()
    return render(request, self.template_name, {'form' : form})

    if form is_valid():
        #Save booking
        booking = form.save(commit=False)
        booking.customer






"""
# View for updating a booking
class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    template_name = 'bookings/booking_edit.html'
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.customer = self.request.user
         
        
        date = form.cleaned_data["booking_date"]
        time = form.cleaned_data["booking_time"]

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my_bookings')

    def test_func(self):
        return self.request.user.is_authenticated


# View for listing bookings
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/my_bookings.html'
    context_object_name = 'bookings'
    ordering = ['booking_date', 'booking_time']

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['tables'] = Table.objects.all()
        return context

    def get_queryset(self):
        return Booking.objects.order_by('booking_date', 'booking_time')

# View for creating a new booking


# View for deleting a booking
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'bookings/booking_defensive.html'
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated
"""