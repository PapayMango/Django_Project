# from http.client import HTTPResponse
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import search_form

def index(request):
#    template = loader.get_template('dl_images/index.html')
   temp = 'dl_images/index.html'
   form = search_form()

#    return HttpResponse(template.render(request))
   return render(request)
# Create your views here.