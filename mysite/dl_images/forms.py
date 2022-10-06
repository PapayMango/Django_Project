from socket import fromshare
from django import forms

class search_form(forms.Form):
    url = forms.CharField(min_length=100,max_length=150)

