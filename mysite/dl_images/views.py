# from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the dl_images index.")
# Create your views here.
