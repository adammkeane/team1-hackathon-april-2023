from django.views.generic import TemplateView, CreateView
from .models import Post, Comment
from django.views import generic
from django.shortcuts import render, get_object_or_404


class ForumView(TemplateView):
    """About page view"""

    template_name = "forum.html"


class PostListView(generic.ListView):
    """List view for displaying all posts"""

    template_name = "forum.html"
    model = Post
    context_object_name = "post_list"
    queryset = Post.objects.filter(approved=True).order_by("-created_at")
    paginate_by = 10


class PostCreateView(generic.CreateView):
    model = Post
    fields = [
        "title",
        "content",
        "category",
    ]


class CommentCreateView(generic.CreateView):
    template_name = "comment_form.html"
    model = Comment
    fields = [
        "content",
    ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        # the post will need to be specified. the below is just for test purposes
        post = get_object_or_404(Post, id=1)
        obj.post = post
        obj.save()      
