from django.http import Http404
from django.views.generic import ListView, FormView, UpdateView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from users import mixins as user_mixins
from . import models, forms


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Post
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "posts"


def read_post(request, id):
    try:
        post = models.Post.objects.get(id=id)
        return render(request, "posts/post_read.html", {"post": post})
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))


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


class EditPostView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Post
    template_name = "posts/post_edit.html"
    fields = (
        "title",
        "content",
    )

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        if post.user.id != self.request.user.id:
            raise Http404()
        return post


@login_required
def delete_post(request, post_id):
    user = request.user
    try:
        post = models.Post.objects.get(id=post_id)
        if post.user.id != user.id:
            messages.error(request, "Can't delete")
        else:
            models.Post.objects.filter(id=post_id).delete()
            messages.success(request, "Post Deleted")
        return redirect(reverse("core:home"))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))
