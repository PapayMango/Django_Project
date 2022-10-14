from email import message
from socket import fromshare
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django import forms

class search_form(forms.Form):
    url = forms.CharField(max_length=150)
    # message = forms.CharField(widget=forms.Textarea,max_length=100)
