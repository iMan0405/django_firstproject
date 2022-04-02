from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.conf import settings

@login_required
def chek_user(request):
    user = request.user
    return render(request, 'chek_auth.html', {'user':user})

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/register_finish.html', {})
    
    return render(request, 'registration/register.html', {'form':form})

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'registration/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            return render(request, 'registration/register_finish.html', {})
    
    return render(request, 'registration/register.html', {'form':form})
