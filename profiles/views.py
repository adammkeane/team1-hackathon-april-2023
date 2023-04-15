from django.views.generic import TemplateView


class ProfileView(TemplateView):
    """Profile page view"""

    template_name = "profile.html"
