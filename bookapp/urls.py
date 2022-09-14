from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_view, name="landing"),
    path("new", views.create, name="create"),
    path("admin_panel", views.admin_panel, name="admin_panel")
]