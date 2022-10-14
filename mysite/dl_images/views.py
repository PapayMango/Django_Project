# from http.client import HTTPResponse
from email import message
from importlib.resources import contents
from re import template
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dl_images.forms import search_form
from django.views import View
from dl_images.soup import dl

def index(request):
#    template = loader.get_template('dl_images/index.html')
   temp = 'dl_images/index.html'
   msg = ""
   if request.method == 'POST':
      form = search_form(request.POST)
      if form.is_valid():
         url = form.cleaned_data['url']
         msg = url
         msg = dl(url)
   form = search_form()
   print("b")
   print(request.method)
   print(request.POST.get('url',None))
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
