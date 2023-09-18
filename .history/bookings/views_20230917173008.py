from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Table, Booking
from .forms import BookingForm

class TableListView(LoginRequiredMixin, ListView):
    model = Table
    template_name = 'table_list.html'

class TableCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Table
    fields = ['table_number', 'party_size', 'availability']
    template_name = 'table_form.html'
    success_url = reverse_lazy('table_list')

    def test_func(self):
        return self.request.user.is_staff  # Check if the user is staff

class TableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Table
    fields = ['table_number', 'party_size', 'availability']
    template_name = 'table_form.html'
    success_url = reverse_lazy('table_list')

    def test_func(self):
        return self.request.user.is_staff  # Check if the user is staff

class TableDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Table
    template_name = 'table_confirm_delete.html'
    success_url = reverse_lazy('table_list')

    def test_func(self):
        return self.request.user.is_staff  # Check if the user is staff

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'

class BookingDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        return render(request, 'booking_detail.html', {'booking': booking})

class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')