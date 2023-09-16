from django.shortcuts import render
# Create your views here.


def base(request):
    return render(request, "homebase.html")

def menu(request):
    return render(request, "home/menu.html")