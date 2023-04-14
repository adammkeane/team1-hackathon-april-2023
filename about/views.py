from django.views.generic import TemplateView


class AboutView(TemplateView):
    """About page view"""

    template_name = "about.html"
