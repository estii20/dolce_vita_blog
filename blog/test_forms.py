from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Comment, Post
from .forms import CommentForm, PostForm
from django_summernote.widgets import SummernoteWidget


class FormsTest(TestCase):
    def setUp(self):
        """
        Create a user for testing
        """
        self.user = User.objects.create_user(
            username='nameistest',
            password='passwordistest'
        )


class TestCommentForm(TestCase):
    """
    Test for comment form
    """

    def test_message_field_is_required(self):
        """
        Tests body field is valid
        """
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Tests comment form fields are the same
        """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestPostForm(TestCase):
    """
    Tests fields on post form
    """

    def test_fields_are_explicit_in_post_metaclass(self):
        """
        Tests fields are equal to post form
        """
        form = PostForm()
        self.assertEqual(form.Meta.fields, ['title', 'category', 'author',
                         'featured_image', 'excerpt', 'content', 'author_bio'])

    def test_post_category_is_required(self):
        """
        Tests that category field is required in post form
        """
        form = PostForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_post_title_is_required(self):
        """
        Tests that title field is required in post form
        """
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_author_is_required(self):
        """
        Tests that author field is not required in post form
        """
        form = PostForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')

    def test_post_content_is_required(self):
        """
        Tests that content field is not required in post form
        """
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_post_form_with_invalid_data(self):
        """
        Tests PostForm submission with invalid data
        """
        data = {}  # no data entered
        form = PostForm(data)
        self.assertFalse(form.is_valid())

    def test_post_form_widget(self):
        """
        Tests if SummernoteWidget is applied to content and author_bio fields
        """
        form = PostForm()
        self.assertIsInstance(form.fields['content'].widget, SummernoteWidget)
        self.assertIsInstance(
            form.fields['author_bio'].widget, SummernoteWidget)
