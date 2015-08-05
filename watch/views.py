from django.shortcuts import render

import requests

from django.http import HttpResponse
# Create your views here.

def index(request):
    # Render main page template here!
    return render(request, 'index.html')
