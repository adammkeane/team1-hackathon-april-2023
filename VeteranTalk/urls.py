"""VeteranTalk URL Configuration"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls"), name="home"),
    path("forum/", include("forums.urls"), name="forums_urls"),
    path("users/", include("django.contrib.auth.urls")),
    path("users/", include("users.urls"), name="users_urls"),
    path("profile/", include("profiles.urls"), name="profiles_urls"),
]
