from django.db import models
from core import models as core_models


class Post(core_models.TimeStampedModel):
    """Custom Post Model"""

    title = models.CharField(default="", max_length=100)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, default=1)
    content = models.TextField(default="", max_length=5000)

    def __str__(self):
        return self.title
