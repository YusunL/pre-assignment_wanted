from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """Custom User Admin"""

    list_display = (
        "id",
        "username",
        "email",
        "is_active",
        "is_superuser",
        "last_login",
    )

    list_filter = (
        "id",
        "username",
        "is_superuser",
        "is_active",
        "user_permissions",
    )
