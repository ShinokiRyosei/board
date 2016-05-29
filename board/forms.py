from django.forms import ModelForm
from board.models import Post
from django import forms
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

