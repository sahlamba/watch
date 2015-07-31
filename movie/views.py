from django.shortcuts import render

import json
import urllib
import requests
import pdb

from django.http import HttpResponse
# Create your views here.
url = 'http://www.omdbapi.com/?t=Game of Thrones&Season=1&Episode=1'

def index(request):
    # Render main page template here!
    return HttpResponse("Yo baby!")

def search(request):
    query = request.GET.get('query')
    search_results = requests.get(url)
    json_results = search_results.json()
    pdb.set_trace()
    return HttpResponse(json_results['Title'])
