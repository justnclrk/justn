from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'sum_content': SummernoteWidget(),
        }
        fields = {'title', 'image', 'content', 'tags'}
        
        field_order = {'title', 'image', 'content', 'tags'}
