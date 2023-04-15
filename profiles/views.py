from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from forums.models import Post
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# class ProfileView(generic.ListView):
#     """Profile page view"""

#     model = User
#     template_name = "profile.html"

#     def get_queryset(self):
#         User.objects.filter(username=self.kwargs.get("id"))


class ProfileView(generic.View):
    def get(self, request, id, *args, **kwargs):
        current_user = get_object_or_404(User.objects, id=id)
        posts = current_user.post_owner.order_by("-created_at")

        return render(
            request,
            "profile.html",
            {
                "current_user": current_user,
                "posts": posts,
            },
        )


class PostDetailView(generic.View):
    def get(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post.objects, id=id)
        comments = post.post_comment.order_by("-created_at")
        if len(comments) > 0:
            no_comments = False
        else:
            no_comments = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "no_comments": no_comments,
            },
        )
