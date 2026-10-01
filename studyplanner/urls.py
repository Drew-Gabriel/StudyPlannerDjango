from django.contrib import admin
from django.urls import path
from planner import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("add/", views.add_task, name="add_task"),
    path("tasks/", views.task_list, name="task_list"),
]
