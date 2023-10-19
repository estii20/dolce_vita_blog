from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'author',
            'featured_image',
            'excerpt',
            'content',
            'author_bio'
        ]

        widgets = {
            'content': SummernoteWidget(),
            'author_bio': SummernoteWidget()
        }
