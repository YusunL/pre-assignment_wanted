from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("write/", views.WritePostView.as_view(), name="write"),
    path("read/<int:id>", views.read_post, name="read"),
    path("edit/<int:id>", views.EditPostView.as_view(), name="edit"),
    path("delete/<int:id>", views.delete_post, name="delete"),
]
