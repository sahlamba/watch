from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    # Render main page template here!
    return HttpResponse("Yo baby!")

def search(request):
    query = request.GET.get('query')
    search_results = 
    return HttpResponse(query)
