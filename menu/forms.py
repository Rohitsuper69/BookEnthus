from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.views import generic

class bookReview_form(forms.ModelForm):
    class Meta:
        model = bookReviews_model
        fields = ['title','author','review']

class todo_form(forms.ModelForm):
    class Meta:
        model = todo_model
        fields = ['title']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter your Search:")

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password1','password2']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['first_name','last_name','email','bio','Interest']

