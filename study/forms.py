from django.forms import ModelForm
from . import models


class PostForm(ModelForm):
    """投稿するためのForm

    """

    class Meta:
        model = models.Post
        fields = ('title', 'content')
