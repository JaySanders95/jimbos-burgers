from django.shortcuts import render
from home.forms import CustomSignupForm
from allauth.account.views import SignupView


class CustomSignupView(SignupView):
    form_class = CustomSignupForm


def home(request):
    return render(request, "home.html")


def menu(request):
    burgers = [
        {
            'burger_name': "The Classic",
            'description': "A flame grilled 6oz Angus beef patty, "
            "monterey jack cheese,lettuce, tomato and cool mayonnaise.",
            'price': "£10.99"
        },
        {
            'burger_name': "The New-Yorker",
            'description': "A buttermilk chicken breast, onion rings,"
            " lettuce and tomato, drizzled with gravy.",
            'price': "£11.99"
        },
        {
            'burger_name': "The Crazy Colonel",
            'description': "A Grilled chicken breast, maple-glazed bacon,"
            " monterey jack cheese and lettuce,"
            " smothered in our house BBQ sauce.",
            'price': "£14.99"
        },
        {
            'burger_name': "The Joker's Pistol",
            'description': "2 6oz Angus beef patties, maple-glazed bacon,"
            " monterey cheese, all the greens and "
            "a joker smile dashing of tomato sauce.",
            'price': "£14.99"
        },
        {
            'burger_name': "The Classic Snr.",
            'description': "Our classic beef burger, with DOUBLE the meat,"
            " yes that's 2 angus 6oz patties, maple-glazed bacon,"
            " lettuce, tomato and cool mayo.",
            'price': "£14.99"
        },
        {
            'burger_name': "The Abomination",
            'description': "A 6oz patty, a grilled chicken breast,"
            " maple-glazed bacon, onion rings, monterey jack cheese,"
            " lettuce and tomato. Then painted with BBQ and cool mayo.",
            'price': "£13.99"
        },
        {
            'burger_name': "The Naked Man",
            'description': "2 Angus beef patties,"
            "lettuce, tomato and your choice of sauce,hold the bun!",
            'price': "£11.99"
        },
        {
            'burger_name': "The Not'chour Cheeze",
            'description': "A grilled chicken breast, jalapenos,"
            " chilli heatwave doritos, pepperjack cheese,"
            " gherkin, sriracha sauce on a brioche bun.",
            'price': "£13.99"
        },
        {
            'burger_name': "The Sloppy Jimbo",
            'description': "2 smashed beef patties, red onion, tomato,"
            " lathered in Jimbo's sloppy house sauce,"
            " on a toasted sesame seed bun.",
            'price': "£13.99"
        },
        {
            'burger_name': "The Vee Gerger",
            'description': "A plant based seitan patty, red onion,"
            " tomato, lettuce, vegan cheeze, with vegan-GF mayonnaise.",
            'price': "£9.99"
        },
    ]

    sides = [
        {
            "side_name": "Fries",
            "description": "Your choice of regular fries.",
            "price": "£2.50"
        },
        {
            "side_name": "Onion Rings",
            "description": "Crispy fried onion rings.",
            "price": "£3.00"

        },
        {
            "side_name": "Coleslaw",
            "description": "Freshly made creamy coleslaw.",
            "price": "£2.00"
        },
        {
            "side_name": "Side Salad",
            "description": "Mixed greens with a light dressing.",
            "price": "£3.50"

        },
        {
            "side_name": "Dirty Fries",
            "description": "Fries with cheese sauce, bacon and jalapenos.",
            "price": "£4.50"

        }
    ]

    drinks = [
        {"drink_name": "Coca-Cola/Diet", "price": "£2.00"},
        {"drink_name": "Fanta", "price": "£2.00"},
        {"drink_name": "Dr.Pepper", "price": "£2.00"},
        {"drink_name": "Iced Coffee", "price": "£4.00"},
        {"drink_name": "5 Dollar shake", "price": "£6.00"},
        {"drink_name": "Water", "price": "£1.50"},
    ]

    context = {'burgers': burgers, 'sides': sides, 'drinks': drinks}
    return render(request, 'menu.html', context)
