from django.shortcuts import render

import json
import urllib
import requests
import pdb
from urllib2 import Request, urlopen

from django.http import HttpResponse
# Create your views here.
#url = 'http://www.omdbapi.com/?'
API_KEY = 'dff18c3dae351bbd69a9af3311e7cfea'
url = 'http://api.themoviedb.org/3/movie/'

#this hash function receives the name of the file and returns the hash code
def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

# Add as necessary, kids!!
video_extensions = [".avi",".mp4",".mkv",".mpg",".mpeg",".mov",".rm",".vob",".wmv",".flv",".3gp"]

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

def show(request):
    movie_id = request.GET.get('query')
    #omdb_query = url + 'i=' + movie_id + '&plot=full&r=json'
    #omdb_request = Request(omdb_query)
    #response_body = urlopen(omdb_request).read()
    headers = {'Accept': 'application/json'}
    tmdb_query = url + movie_id + '?api_key=' + API_KEY
    tmdb_request = Request(tmdb_query, headers = headers)
    response_body = urlopen(tmdb_request).read()
    # Send json response to frontend
    try:
        return HttpResponse(json.dumps(response_body), content_type = "application/json")
    except:
        return HttpResponse(json.dumps({ "error": "Check the movie Id" }), content_type = "application/json")
def subtitles(request):
    file_name = request.GET.get('query')
    file_name = remove_ext(file_name)
    filename_hash = get_hash(file_name)
    headers = { 'User-Agent' : 'SubDB/1.0 (subtitle-downloader/1.0; http://github.com/amanthedorkknight/subtitleDownloader)' }
    query_link = "http://api.thesubdb.com/?action=download&hash=" + filename_hash + "&language=en"
    subDB_query = query_link
    subDB_request = Request(subDB_query, headers)
    response_sub = urlopen(subDB_request).read()
    return HttpResponse(json.dumps(response_sub), content_type = "application/json")
