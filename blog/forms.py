from .models import Comment, Post
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    Form for comments
    """
    class Meta:
        """Form fields"""
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Form for posts
    """
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

        featured_image = CloudinaryFileField()
