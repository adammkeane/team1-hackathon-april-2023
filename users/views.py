""" Users app views """
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    form = UserCreationForm()
    return render(request, "authenticate/signup.html", {"sign_up_form": form})


def login_user(request):
    return render(request, 'authenticate/login.html', {})
