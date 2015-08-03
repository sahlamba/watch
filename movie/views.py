from django.shortcuts import render

import json
import urllib
import requests
import pdb

from django.http import HttpResponse
# Create your views here.
url = 'http://www.omdbapi.com/?'

def index(request):
    # Render main page template here!
    return render(request, 'templates/index.html')

# API views
def search(request):
    query = request.GET.get('query')
    search_url = url + 's=' + query + '&type=movie'
    search_results = requests.get(search_url)
    json_results = search_results.json()
    return HttpResponse(json_results['Search'])

def show(request):
    movie_id = request.GET.get('query')
    show_url = url + 'i=' + movie_id + '&plot=short&r=json&tomatoes=true'
    show_data = requests.get(show_url)
    json_show = show_data.json()
    return HttpResponse(json_show)
