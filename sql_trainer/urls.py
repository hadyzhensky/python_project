"""URL configuration for sql_trainer project."""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from trainer import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("admin/", admin.site.urls),
    path("trainer/", include("trainer.urls")),
    path("login/", auth_views.LoginView.as_view(
        template_name="trainer/login.html"
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"),
         name="logout"),
    path("signup/", views.signup_view, name="signup"),
]

