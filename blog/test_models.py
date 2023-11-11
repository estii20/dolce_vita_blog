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
        """
        Create test data
        """
        self.user = User.objects.create(username='nameistest')
        self.user.set_password('passwordistest')
        self.user.save()

        # Create a category for testing
        self.category = Category.objects.create(
            name=1
        )

        # Create an author bio for testing
        self.author_bio = AuthorBio.objects.create(
            author_bio='Test Author Bio')

        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            category_id=1,
            content='test content',
            excerpt='test excerpt',
            featured_image='test.jpeg',
            author_bio='Test Author Bio',
            status=1,  # Published
        )

        self.comment = Comment.objects.create(
            post=self.post,
            name=self.user,
            body='test comment'
        )

    def test_category_model(self):
        """
        Test Category model
        """
        category = Category.objects.get(name=1)
        self.assertEqual(str(category), '1')

    def test_author_bio_model(self):
        """
        Test AuthorBio model
        """
        author_bio = AuthorBio.objects.get(author_bio='Test Author Bio')
        self.assertEqual(str(author_bio), 'Test Author Bio')

    def test_post_model(self):
        """
        Test Post model
        """
        post = Post.objects.get(title='Test Post')
        self.assertEqual(str(post), 'Test Post')
        self.assertEqual(post.number_of_likes(), 0)

    def test_comment_model(self):
        """
        Test Comment model
        """
        comment = Comment.objects.create(
            post=self.post,
            name=self.user,
            email='test@example.com',
            body='Test comment body',
            approved=True
        )
        self.assertEqual(
            str(comment), f'Comment Test comment body by {self.user}')

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
