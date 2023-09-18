from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Table, Booking
from .forms import BookingForm

class TableListView(ListView):
    model = Table
    template_name = 'table_list.html'

class TableCreateView(CreateView):
    model = Table
    fields = ['table_number', 'party_size', 'availability']
    template_name = 'table_form.html'
    success_url = reverse_lazy('table_list')

class TableUpdateView(UpdateView):
    model = Table
    fields = ['table_number', 'party_size', 'availability']
    template_name = 'booking_edit.html'
    success_url = reverse_lazy('table_list')

class TableDeleteView(DeleteView):
    model = Table
    template_name = 'table_confirm_delete.html'
    success_url = reverse_lazy('table_list')

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'

class BookingDetailView(View):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        return render(request, 'booking_detail.html', {'booking': booking})

class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')