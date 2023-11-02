from django.test import TestCase
from .forms import CommentForm, PostForm


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
    Test fields on post form
    """
    def test_fields_are_explicit_in_post_metaclass(self):
        """
        Test fields are equal to post form
        """
        form = PostForm()
        self.assertEqual(form.Meta.fields, ['title', 'category', 'author',
                         'featured_image', 'excerpt', 'content', 'author_bio'])

    def test_post_content_is_required(self):
        """
        Tests that category field is required in post form
        """
        form = PostForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')
