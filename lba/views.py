from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request):    
    return HttpResponse("test Hello World")

def helloworld(request):        
    return render(request, "lba/helloworld.html")

def home(request):        
    return render(request, "lba/home.html")
