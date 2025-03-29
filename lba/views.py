from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):    
    return HttpResponse("Hello World")

def helloworld(request):        
    return render(request, "lba/helloworld.html")
