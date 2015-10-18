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

# API views
def search(request):
    query = request.GET.get('query')
    headers = { 'Accept': 'application/json' }
    url_search = 'http://api.themoviedb.org/3/search/movie?api_key=' + API_KEY + '&query=' + query;
    request = Request(url_search , headers = headers)
    response_body = urlopen(request).read()
    response_body = json.loads(response_body)
    response_body["results"] = [item for item in response_body["results"] if str(item["poster_path"]) != 'None']
    for obj in response_body["results"]:
        obj["poster_path"] = 'http://image.tmdb.org/t/p/original' + str(obj["poster_path"])
    return HttpResponse(json.dumps(response_body), content_type = "application/json")

def youtube_vid(movie_id):
    headers = { 'Accept': 'application/json' }
    trailer_query = url + movie_id + '/videos' + '?api_key=' + API_KEY
    trailer_request = Request(trailer_query, headers = headers)
    response_body = urlopen(trailer_request).read()
    response_body = json.loads(response_body)
    trailer_url = 'https://www.youtube.com/watch?v=' + str(response_body["results"][0]["key"])
    return trailer_url

def credits(movie_id):
    headers = { 'Accept': 'application/json' }
    credits_url = url + movie_id + '/credits' + '?api_key=' + API_KEY
    credits_request = Request(credits_url, headers = headers)
    credits_body = urlopen(credits_request).read()
    credits_body = json.loads(credits_body)
    return credits_body

def show(request):
    try:
        # TMDB API Start
        movie_id = request.GET.get('query')
        headers = { 'Accept': 'application/json' }
        tmdb_query = url + movie_id + '?api_key=' + API_KEY
        tmdb_request = Request(tmdb_query, headers = headers)
        response_body = urlopen(tmdb_request).read()
        trailer = youtube_vid(movie_id)
        response_body = json.loads(response_body)
        response_body["trailer"] = trailer
        #returning image using poster path and backdrop path
        response_body["poster"] = 'http://image.tmdb.org/t/p/original' + str(response_body["poster_path"])
        response_body["backdrop"] = 'http://image.tmdb.org/t/p/w1280' + str(response_body["backdrop_path"])
        #in trailer link of trailer is stored, in subtitle subtitle url is saved
        subtitle_url = subtitles(str(response_body["original_title"]))
        credits_body = credits(movie_id)
        #start of cast
        full_cast = []
        for cast in credits_body["cast"][:5]:
            full_cast.append({"character": str(cast["character"]), "name": str(cast["name"]), "photo": 'http://image.tmdb.org/t/p/original' + str(cast["profile_path"])})
        #end of cast
        # start of crew
        full_crew = [crew for crew in credits_body["crew"] if str(crew["job"]) == 'Director']
        full_crew = [{"job": str(crew["job"]), "name": str(crew["name"]), "photo": 'http://image.tmdb.org/t/p/original' + str(crew["profile_path"])} for crew in full_crew]
        response_body["cast"] = full_cast
        response_body["crew"] = full_crew
        response_body["subtitle"] = subtitle_url
        # TMDB API End
        # YTS API Start
        yts_url = urlopen('https://yts.to/api/v2/list_movies.json?movie_count=1').read()
        torrents = json.loads(yts_url)["data"]["movies"][0]["torrents"]
        for torrent in torrents:
            response_body[str(torrent["quality"])] = str(torrent["url"])
        # YTS API End
        # Send json response to frontend
        return HttpResponse(json.dumps(response_body), content_type = "application/json")
    except:
        return HttpResponse(json.dumps({ "error": "Check the movie ID" }), content_type = "application/json")

def subtitles(title):
    # convert title here
    title = title.replace(' ', '-').lower()
    url = 'http://subscene.com/subtitles/' + title
    return url
