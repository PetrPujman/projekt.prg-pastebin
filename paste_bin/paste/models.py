from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


formats = [("python", "Python"),
           ("html", "HTML"),
           ("javascript", "Javascript"),
           ("css", "CSS"),
           ("c", "C"),
           ("c++", "C++"),
           ("csharp", "CSharp"),
           ("sql", "SQL"),
           ("php", "PHP"),
           ("bash", "Bash")]


def generate_slug():
    return token_urlsafe()[:8]


class Content(models.Model):
    name = models.CharField(max_length=30)
    text_format = models.CharField(max_length=10, choices=formats, null=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=8, default=generate_slug, unique=True)

    def formatted_text(self):
        lexer = get_lexer_by_name(self.text_format, stripall=True)
        formatter = HtmlFormatter(linenos=True, cssclass="source")
        return highlight(self.text, lexer, formatter)


    def __str__(self):
        return self.name

