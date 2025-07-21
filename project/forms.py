from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django import forms

class Signform(UserCreationForm):

    email=forms.EmailField()
   
    username=forms.CharField(max_length=200)
    first_name=forms.CharField(max_length=200)
    class Meta:
       model=User
       fields=[
            'username','first_name','email'
        ]
