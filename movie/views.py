from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    # Render main page template here!
    return HttpResponse("Yo baby!")
