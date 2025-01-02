from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect_to_login, name="redirect_to_login"),
    path("login", views.login_view, name="login"),
    path("home", views.home, name = "home"),
    path("logout", views.logout_view, name = "logout"),
    path("register", views.register, name = "register"),
]