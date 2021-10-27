from django.http import Http404
from django.views.generic import (
    ListView,
    FormView,
)
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
from . import models, forms


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Post
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "posts"


@login_required
class WritePostView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.WritePostForm
    template_name = "posts/post_write.html"

    def form_valid(self, form):
        post = form.save()
        post.writer = self.request.user
        post.save()
        form.save_m2m()
        messages.success(self.request, "Post Uploaded")
        return redirect(reverse("core:home"))
