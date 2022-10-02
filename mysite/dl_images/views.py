# from http.client import HTTPResponse
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
#    template = loader.get_template('dl_images/index.html')

#    return HttpResponse(template.render(request))
   return render(request,'dl_images/index.html')
# Create your views here.