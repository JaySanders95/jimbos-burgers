from django.shortcuts import renderHttpResponse
from django.http import 
# Create your views here.


def index(request):
    return HttpResponse("hello")