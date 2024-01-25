from django.forms import ModelForm

from .models import Content


class ContentForm(ModelForm):
    class Meta:
        model = Content
        exclude = ["user", "slug"]

