from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader, RequestContext
from board.forms import PostForm, SignupForm, LoginForm
# Create your views here.

def  index(request):
    return HttpResponse('Hello World')

def signup(request):
    user = User()
    template = loader.get_template('signup.html')
    form = SignupForm
    return render_to_response(template, {'form': form}, context_instance=RequestContext(request))