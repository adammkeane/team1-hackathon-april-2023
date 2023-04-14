from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    form = UserCreationForm()
    return render(request, "users/signup.html", {"sign_up_form": form})
