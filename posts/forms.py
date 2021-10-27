from django import forms
from . import models


class WritePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = (
            "title",
            "content",
        )

    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        return post
