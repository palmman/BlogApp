from dataclasses import field
from re import A
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article

class LoginForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
class AddArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'description']
        
class AddUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'description']
        