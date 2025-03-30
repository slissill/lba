from django.shortcuts import render
from .models import Artist
from .api_spotify import *

# Create your views here.
from django.http import HttpResponse

def test(request):    
    return HttpResponse("test Hello World")

def helloworld(request):        
    return render(request, "lba/helloworld.html")

def home(request):
    artists = Artist.objects.all()
    return render(request, "lba/home.html", {'artists': artists})

def artist(request, artist_name):
    datas = get_infos_artist(artist_name)
    return render(request, "lba/artist.html", {'datas' : datas})

def album(request, album_id):
    tracks = get_tracks_by_album(album_id)
    return render(request, "lba/album.html", {'tracks' : tracks})