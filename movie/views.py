from django.shortcuts import render

import json
import urllib
import requests
import pdb
from urllib2 import Request, urlopen

from django.http import HttpResponse
# Create your views here.
url = 'http://www.omdbapi.com/?'

# API views
def search(request):
    query = request.GET.get('query')
    search_url = url + 's=' + query + '&type=movie'
    search_results = requests.get(search_url)
    json_results = search_results.json()
    return HttpResponse(json_results['Search'])

def show(request):
    movie_id = request.GET.get('query')
    omdb_query = url + 'i=' + movie_id + '&plot=full&r=json'
    omdb_request = Request(omdb_query)
    response_body = urlopen(omdb_request).read()
    # Send json response to frontend

def subtitles(request):
    file_name = request.GET.get('query')
    # Store the hash of file_name in movie_name_hash
    movie_name_hash = get_hash(file_name)


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
    # time for some cool coding bitch!!
    for ext in video_extensions return filename.replace(ext, "") if (filename.replace(ext, "") != filename)
    
