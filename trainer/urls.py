from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('check/<int:task_id>/', views.check_sql, name='check_sql'),
]