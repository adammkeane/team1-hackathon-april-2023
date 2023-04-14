from django.urls import path
from . import views


urlpatterns = [
    path("", views.ForumView.as_view(), name="forum"),
]
