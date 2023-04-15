from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<slug:id>/comment/", views.CommentCreateView.as_view(), name="comment_create"),
    path("post/<slug:id>/", views.PostDetailView.as_view(), name='post_detail'),
]
