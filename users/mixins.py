from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Can't do that")
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):

    login_url = reverse_lazy("users:login")
