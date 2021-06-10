from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['text', 'title']


class CreateImgNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['img']


class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['video', 'title_img']
