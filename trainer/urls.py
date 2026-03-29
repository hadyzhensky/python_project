"""URL configuration for trainer app."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.task_list_view, name="task_list"),
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),
    path("progress/", views.progress_view, name="progress"),
    path("profile/", views.profile_view, name="profile"),
]
