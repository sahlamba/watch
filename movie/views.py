from django.shortcuts import render

import json
import urllib
import requests
import pdb
from urllib2 import Request, urlopen

from django.http import HttpResponse
# Create your views here.
API_KEY = 'dff18c3dae351bbd69a9af3311e7cfea'
url = 'http://api.themoviedb.org/3/movie/'

def remove_ext(filename):
    # time for some cool coding, bitch!!
    for ext in video_extensions:
        filename = filename.replace(ext, "")
    return filename
    # hash = get_hash(filename)

# API views
# def search(request):
#     query = request.GET.get('query')
#     search_url = url + 's=' + query + '&type=movie'
#     search_results = requests.get(search_url)
#     json_results = search_results.json()
#     #return HttpResponse(json_results['Search'])

def youtube_vid(movie_id):
    headers = { 'Accept': 'application/json' }
    trailer_query = url + movie_id + '/videos' + '?api_key=' + API_KEY
    trailer_request = Request(trailer_query, headers = headers)
    response_body = urlopen(trailer_request).read()
    response_body = json.loads(response_body)
    return response_body

def show(request):
    try:
        movie_id = request.GET.get('query')
        headers = {'Accept': 'application/json'}
        tmdb_query = url + movie_id + '?api_key=' + API_KEY
        tmdb_request = Request(tmdb_query, headers = headers)
        response_body = urlopen(tmdb_request).read()
        trailer = youtube_vid(movie_id)
        response_body = json.loads(response_body)
        response_body["trailer"] = trailer
        #in trailer link of trailer is stored, in subtitle subtitle url is saved
        subtitle_url = subtitles(str(response_body["original_title"]))
        response_body["subtitle"]=subtitle_url
        # Send json response to frontend
        return HttpResponse(json.dumps(response_body), content_type = "application/json")
    except:
        return HttpResponse(json.dumps({ "error": "Check the movie Id" }), content_type = "application/json")

def subtitles(title):
    # convert title here
    title = title.replace(' ', '-').lower()
    url = 'http://subscene.com/subtitles/' + title
    return url
