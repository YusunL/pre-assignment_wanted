from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """Custom Post Admin"""

    list_display = (
        "title",
        "user",
        "created",
        "updated",
    )

    list_filter = ("user",)
