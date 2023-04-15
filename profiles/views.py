from django.views import generic
from django.contrib.auth.models import User


class ProfileView(generic.ListView):
    """Profile page view"""

    model = User
    template_name = "profile.html"

    def get_queryset(self):
        User.objects.filter(username=self.kwargs.get("id"))


# from django.shortcuts import render
# from django.contrib.auth.models import User

# def profile_view(request):
#     current_user = request.user
#     posts = request.g
