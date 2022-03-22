from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
def home_view(request):
    return render(request, 'home.html', {})