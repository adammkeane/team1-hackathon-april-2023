""" Users app views """
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    form = UserCreationForm()
    return render(request, "authenticate/signup.html", {"sign_up_form": form})


def login_user(request):
    if request.method == "POST":
        """
        Code from Django docs
        https://docs.djangoproject.com/en/3.2/topics/auth/default/#auth-web-requests
        lines 19-23
        """
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Login error. Try again..."))
            # messages.success(request, ("Login error. Try again..."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logout succesful. Good bye..."))
    return redirect('home')
