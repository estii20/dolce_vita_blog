from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment, Category, AuthorBio
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin


class AdminTest(TestCase):
    def setUp(self):
        """
        Create a superuser for testing
        """
        # Create a superuser for testing
        self.user = User.objects.create_superuser(
            username='adminuser', 
            password='adminpassword', 
            email='admin@dolcevita.com')
        self.client = Client()
        self.client.login(username='adminuser', password='adminpassword')

        # Create test instances
        self.category = Category.objects.create(name='1')
        self.author_bio = AuthorBio.objects.create(
            author_bio='Test Author Bio')

    def test_post_admin(self):
        """
        Tests PostAdmin configurations
        """
        post_admin = admin.site._registry[Post]
        self.assertIsInstance(post_admin, SummernoteModelAdmin)
        self.assertEqual(post_admin.list_display,
                         ('title', 'slug', 'status', 'created_on'))
        self.assertEqual(post_admin.search_fields, ['title', 'content'])
        self.assertEqual(post_admin.list_filter, ('status', 'created_on'))
        self.assertEqual(post_admin.prepopulated_fields, {'slug': ('title',)})
        self.assertEqual(post_admin.summernote_fields, ('content',))

    def test_comment_admin(self):
        """
        Tests CommentAdmin configurations
        """
        comment_admin = admin.site._registry[Comment]
        self.assertEqual(comment_admin.list_display,
                         ('name', 'body', 'post', 'created_on', 'approved'))
        self.assertEqual(comment_admin.list_filter, ('approved', 'created_on'))
        self.assertEqual(comment_admin.search_fields,
                         ('name', 'email', 'body'))

    def test_approve_comments_action(self):
        """
        Tests the approve_comments action in CommentAdmin
        """
        post = Post.objects.create(
            title='Test Post',
            category=self.category,
            slug='test-post',
            author=self.user,
            excerpt='Test excerpt',
            content='Test content',
            status=1,  # Published
            author_bio='Test author bio'
        )
        comment = Comment.objects.create(
            post=post,
            name=self.user,
            email='test@example.com',
            body='Test comment body',
            approved=False
        )

    def test_category_model_and_author_bio_registered(self):
        """
        Tests Category model and AuthorBio registration in admin
        """
        self.assertIn(Category, admin.site._registry)
        self.assertIn(AuthorBio, admin.site._registry)
