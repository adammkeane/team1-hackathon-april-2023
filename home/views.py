from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Homepage view"""

    template_name = "home.html"
