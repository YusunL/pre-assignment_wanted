from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("write/", views.WritePostView.as_view(), name="write"),
    path("read/<int:id>", views.ReadPostView, name="read"),
]
