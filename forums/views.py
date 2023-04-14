from django.views.generic import TemplateView
from .models import Post
from django.views.generic.list import ListView


class ForumView(TemplateView):
    """About page view"""

    template_name = "forum.html"


class PostListView(ListView):
    """List view for displaying all posts"""

    template_name = "forum.html"
    model = Post
    context_object_name = "post_list"
    queryset = Post.objects.filter(approved=True).order_by("-created_at")
    paginate_by = 10
