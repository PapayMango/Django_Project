# from http.client import HTTPResponse
from email import message
from importlib.resources import contents
from re import template
import re
from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dl_images.forms import search_form
from django.views import View
from dl_images.soup import dl
from django.http import JsonResponse

process = 0
total = 0

def index(request):
   aj = request.headers.get('x-requested-with') == 'XMLHttpRequest'
   # print("ajax : " + str(request.headers.get('x-requested-with') == 'XMLHttpRequest'))

   temp = 'dl_images/index.html'
   msg = ""
   d = False

   if request.method == 'POST' and not aj:

      form = search_form(request.POST)

      msg = request
      if form.is_valid():
         url = form.cleaned_data['url']
         d = dl(url)
         sleep(3)
   form = search_form()

   # print(request.method)
   # print(request.POST.get('url',None))

   if aj:
      return JsonResponse({'p':process,'t':total,'s':d})

   return render(request,temp,{'form':form,'message':msg})

def set_process(i):
   global process
   process = i
   return i
def set_total(i):
   global total
   total = i
   return i