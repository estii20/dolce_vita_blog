from django.test import TestCase
from .models import Post, Comment, AuthorBio, Category
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify


User = get_user_model()


class TestModels(TestCase):
    """
    Test blog app models
    """
    @classmethod
    def setUpTestData(self):
        """Create test data"""
        self.user = User.objects.create(username='nameistest')
        self.user.set_password('passwordistest')
        self.user.save()
        self.category = Category.objects.create(
            name=1
        )

        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            category_id=1,
            content='test content',
            excerpt='test excerpt',
            featured_image='test.jpeg',
            author_bio='This is a test author bio',
            status=1
        )

        self.comment = Comment.objects.create(
            post=self.post,
            name=self.user,
            body='test comment'
        )

    def test_comment_model_str(self):
        """
        Test the __str__ method for comment
        """
        self.assertEqual(
            self.comment.__str__(),
            f'Comment {self.comment.body} by {self.comment.name}'
        )

    def test_post_and_comment_approved(self):
        """
        Test for Comment and post is an approved field
        """
        self.assertTrue(self.post.status == 1)
        self.assertFalse(self.comment.approved)

    def test_absolute_url_str(self):
        """
        Test absolute_url for post
        """
        self.assertEqual(self.post.get_absolute_url(),
                         f'/post/{self.post.slug}/')

    def test_post_model__category_str(self):
        """
        Test the __str__ method for category post
        """
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_post_model__title_str(self):
        """Test the __str__ method for post"""
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_slug_value_for_title(self):
        """
        Test that two posts with identical titles 
        don't get assigned the same slug.
        """
        self.assertEqual(self.post.slug, slugify(self.post.title))
