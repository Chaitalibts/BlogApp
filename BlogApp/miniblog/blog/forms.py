
from dataclasses import field
from tkinter import Widget
from tkinter.ttk import Style
from django import forms
from django.forms import ImageField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post


class SignUpForm(UserCreationForm):

    password1 = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={'class': 'form-control m-2'}))

    password2 = forms.CharField(label='confirm password(Retype)', widget=forms.PasswordInput(
        attrs={'class': 'form-control m-2'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control m-2 w-50'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control m-2 w-50'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control m-2 w-50'}),
            'email': forms.EmailInput(attrs={'class': 'form-control m-2 w-50'}),
        }


class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control m-2'}))

    password = forms.CharField(label=_("password"), strip=False,
                               widget=forms.TextInput(attrs={'autocomplete': True, 'class': 'form-control m-2'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {'title': 'Title', 'category': 'Category',
                  'desc': 'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }
        image = forms.ImageField(
            label='Images', widget=forms.ClearableFileInput({'class': 'form-control'}))
        
