from django.shortcuts import render
# Create your views here.


def base(request):
    return render(request, "base.html")

def menu(request):
    return render(request, "menu.html")