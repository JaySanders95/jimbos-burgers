from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, "home.html")


def menu(request):
    return render(request, "menu.html")

def menu_items


def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
    if form.is_valid():
        # Create a new booking object but don't save it yet
        new_booking = form.save(commit=False)

        # You might want to perform additional processing here

        # Save the booking to the database
        new_booking.save()
        # Redirect to the booking list page after successful submission
        return redirect('booking_list')
    else:
        form = BookingForm()

    return render(request, "booking_add.html")

def my_bookings(request):
    return render(request, "my_bookings.html")
