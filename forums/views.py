from django.views.generic import TemplateView
from .models import Post, Comment
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


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
    template_name = "post_create.html"

    model = Post
    fields = [
        "title",
        "content",
        "category",
    ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        # the post will need to be specified. the below is just for test purposes
        # post = get_object_or_404(Post, id=self.get_queryset())
        post = get_object_or_404(Post, id=1)
        obj.post = post
        obj.save()
        return HttpResponseRedirect("../")


class CommentCreateView(generic.CreateView):
    template_name = "comment_form.html"
    model = Comment
    fields = [
        "content",
    ]

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs.get("id"))

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        post = get_object_or_404(Post, id=self.kwargs.get('id'))
        obj.post = post
        obj.save()
        return HttpResponseRedirect(reverse('post_detail', kwargs={'id': post.id}))

    def test_func(self):
        return self.request.user.is_authenticated


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
