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
   print("ajax : " + str(request.headers.get('x-requested-with') == 'XMLHttpRequest'))
#    template = loader.get_template('dl_images/index.html')
   temp = 'dl_images/index.html'
   msg = ""
   d = False

   if request.method == 'POST' and not aj:
      # if aj:
      #    # return HttpResponse('aaa')
      #    return JsonResponse({'a':'aaa','b':'bbb'})
      form = search_form(request.POST)
      # print(form)
      msg = request
      if form.is_valid():
         url = form.cleaned_data['url']
         d = dl(url)
         sleep(3)
   form = search_form()
   print("b")
   print(request.method)
   print(request.POST.get('url',None))

   if aj:
      return JsonResponse({'p':process,'t':total,'s':d})

   # print(request.POST.get('message',None))
   # msg = request.POST.get('message',None)
#    return HttpResponse(template.render(request))
   return render(request,temp,{'form':form,'message':msg})
# Create your views here.

# class HelloView(View):
#    def get(self,request,*args,**kwargs):
#       context = {
#          'message':"Hello World get method"
#       }
#       print("c")
#       return render(request,'dl_images/hello.html',context)
#    def post(self,request,*args,**kwargs):
#       context = {
#          'message':"Hello World post method"
#       }
#       print("a")
#       return render(request,'dl_images/hello.html',context)
# hello = HelloView.as_view()
# print("d")

def set_process(i):
   global process
   process = i
   return i
def set_total(i):
   global total
   total = i
   return i