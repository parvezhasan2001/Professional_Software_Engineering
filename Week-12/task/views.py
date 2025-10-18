from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request, name):
    return HttpResponse(f" <h1>Welcome {name} to Django!</h1>")