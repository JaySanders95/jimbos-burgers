from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bookings.models import Booking, Table, TIME_CHOICES
from bookings.forms import BookingForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from datetime import datetime


class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bookings/booking_add.html'
    form_class = BookingForm
    model = Booking

    def form_valid(self, form):
        try:
            # Customer who is logged in is owner of booking request
            form.instance.customer = self.request.user

            capacity = form.cleaned_data['num_guests']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            notes = 

            time_choice = dict(TIME_CHOICES)

            if date < timezone.now().date():
                raise ValueError("You can't book tables in the past.")

            # Checks date if booking date is not today or in the future


            table = self.find_free_table(capacity, date, time)

            # Creates booking
            if table:
                booking = Booking.objects.create(
                    table=table,
                    date=date,
                    time=time,
                    customer=self.request.user,
                    num_guests=capacity,
                )
                booking.save()
                messages.success(self.request, "Booking completed successfully!")
                # Sends email if table requirements are met
                return redirect('my_bookings')
            else:
                messages.error(self.request, "Your booking could not be made, please try a different time.")
                return render(self.request, self.template_name, {'form': form})

        except ValueError as e:
            messages.error(self.request, str(e))
            return render(self.request, self.template_name, {'form': form})

        except Http404:
        #Handle 404 error
            return HttpResponseNotFound(render(self.request, '404.html'))

        except PermissionDenied:
        #Handle 403 error
            return HttpResponseForbidden(render(self.request, '403.html'))

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
        if user.is_staff:
            return Booking.objects.all().order_by('date', 'time')
        
        else:
            return Booking.objects.filter(customer=user).order_by('date', 'time')


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_edit.html'
    success_url = reverse_lazy('my_bookings')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj
    
    
    def form_valid(self, form):
        try:

            form.instance.customer = self.request.user

            capacity = form.cleaned_data['num_guests']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            booking = form.save(commit=False)
            

            #Finds free table based on the parameters (num_guests, date, time)
            new_table = self.find_free_table(booking.num_guests, booking.date, booking.time)
            if new_table:
                booking.table = new_table
                booking.save()
                messages.success(self.request, "Booking updated!")
                return super().form_valid(form)
            else:
                messages.error(self.request, "Booking could not be updated, please try again.")
                return render(self.request, self.template_name, {'form':form})
        
        except ValueError as e:
            messages.error(self.request, str(e))
            return render(self.request, self.template_name, {'form': form})

        except Http404:
        #Handle 404 error
            return HttpResponseNotFound(render(self.request, '404.html'))

        except PermissionDenied:
        #Handle 403 error
            return HttpResponseForbidden(render(self.request, '403.html'))

        

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

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'bookings/booking_defensive.html'
    success_url = reverse_lazy('my_bookings')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Booking deleted.")
        return super().delete(request, *args, **kwargs)
