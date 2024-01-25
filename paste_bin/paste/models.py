from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe


def generate_slug():
    return token_urlsafe()[:8]


class Content(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=8, default=generate_slug, unique=True)

    def __str__(self):
        return self.name
