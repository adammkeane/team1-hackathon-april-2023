from django.views.generic import TemplateView


class ForumView(TemplateView):
    """About page view"""

    template_name = "forum.html"
