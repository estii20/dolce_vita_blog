from django.test import TestCase
from .models import Post, Comment, AuthorBio, Category
from django.contrib.auth import get_user_model


# Create your tests here.
USER_MODEL = get_user_model()


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
            author_bio='This is a test author bio'
        )

        self.comment = Comment.objects.create(
            post=self.post,
            username=self.user,
            message='test comment'
        )

        self.read_time = self.content.split(' ') / 250
