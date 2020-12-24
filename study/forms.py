from django.forms import ModelForm
from . import models


class PostForm(ModelForm):
    """投稿するためのForm

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.Post
        fields = ('title', 'content')
