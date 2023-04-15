""" Users app URL Configuration """
from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('signup', views.sign_up, name='signup'),
]
