from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, "home.html")


# def menu(request):
    # return render(request, "menu.html")

def menu(request):
    burgers = [
        {
            'burger_name': "The Classic",
            'description': "A flame grilled 6oz Angus beef patty, monterey jack cheese, lettuce, tomato and cool mayonnaise.",
            price: "£10.99"
        },
        {
            'burger_name': "The New-Yorker",
            'description': "A buttermilk chicken breast, onion rings, lettuce and tomato, drizzled with gravy.",
            'price': "£11.99"
        },
        {
            'burger_name': "The Joker's Pistol",
            'description': "A Grilled chicken breast, maple-glazed bacon, monterey jack cheese and lettuce, smothered in our house BBQ sauce.",
            'price': "£14.99"
        },
        {
            'burger_name': "",
            'description': "2 6oz Angus beef patties, maple-glazed bacon, monterey cheese, all the greens and a joker smile dashing of tomato sauce.",
            'price': "£14.99"
        },
        {
            'burger_name': "The Classic Snr.",
            'description': "Our classic beef burger, with DOUBLE the meat, yes that's 2 angus 6oz patties, maple-glazed bacon, lettuce, tomato and cool mayo.",
            'price': "£14.99"
        },
        {
            'burger_name': "The Abomination",
            'description': "A 6oz patty, a grilled chicken breast, maple-glazed bacon, onion rings, monterey jack cheese, lettuce and tomato. Then painted with BBQ and cool mayo.",
            'price': "£13.99"
        },
        {
            'burger_name': "The Naked Man",
            'description': "2 Angus beef patties, lettuce, tomato and your choice of sauce, hold the bun!",
            'price': "£11.99"
        },
        {
            'burger_name': "The Not'chour Cheeze",
            'description': "A grilled chicken breast, jalapenos, chilli heatwave doritos, pepperjack cheese, gherkin, sriracha sauce on a brioche bun.",
            'price': "£13.99"
        },
        {
            'burger_name': "The Sloppy Jimbo",
            'description': "2 smashed beef patties, red onion, tomato, lathered in Jimbo's sloppy house sauce, on a toasted sesame seed bun.",
            'price': "£13.99"
        },
        {
            'burger_name': "<i class='fa-solid fa-leaf'>The Vee Gerger</i>",
            'description': "A plant based seitan patty, red onion, tomato, lettuce, vegan cheeze, with vegan-GF mayonnaise.",
            'price': "£9.99"
        },
    ]

    context = {'burgers': burgers}
    return render(request, 'menu.html', context)


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
