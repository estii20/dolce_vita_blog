from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Comment, Category, AuthorBio
from .views import PostList, PostDetail, PostLike, AddPost, EditPost, DeletePost, CategoryView, CommentDeleteView, CommentEdit, AboutView


User = get_user_model()


class TestModels(TestCase):
    """
    Test blog app models
    """
    @classmethod
    def setUpTestData(self):
        """Create test data"""
        # Create a user for testing
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

        # Create a post for testing
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            category_id=1,
            content='test content',
            excerpt='test excerpt',
            featured_image='test.jpeg',
            author_bio='This is a test author bio',
            status=1  # Published
        )

        # Create a comment for testing
        self.comment = Comment.objects.create(
            post=self.post,
            name=self.user,
            body='test comment'
        )

        self.factory = RequestFactory()

    def test_get_view_post_list(self):
        """
        Test to get homepage and template index.html
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_get_post_detail_view(self):
        """ 
        Test to get Post Detail page and template post_detail.html
        """
        response = self.client.get(
            reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')

    def test_get_view_add_post(self):
        """
        Test to get Add Post page and template add_post.html
        """
        self.client.login(username='nameistest', password='passwordistest')
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html', 'base.html')

    def test_get_view_edit_post(self):
        """
        Test to get Edit Post page and template post_detail.html
        """
        self.client.login(username='nameistest', password='passwordistest')
        response = self.client.get(
            reverse('post_edit', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_edit.html', 'base.html')

    def test_get_view_post_delete(self):
        """
        Test to get Post Delete page and template post_delete.html
        """
        self.client.login(username='nameistest', password='passwordistest')
        response = self.client.get(
            reverse('post_delete', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_delete.html', 'base.html')

    def test_view_post_comment(self):
        """
        Test comments for posts
        """
        self.client.login(username='nameistest', password='passwordistest')
        response = self.client.post(
            reverse('post_detail',
                    args=[self.post.slug]),
            data={'body': 'testcomment'})
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))

    def test_comment_edit_view(self):
        """
        Tests CommentEdit view
        """
        self.client.login(username='nameistest', password='passwordistest')
        response = self.client.get(
            reverse('comment_edit', args=['test-post', self.comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comment_edit.html')

    def test_comment_delete_view(self):
        """
        Tests CommentDeleteView
        """
        self.client.login(username='nameistest', password='passwordistest')
        response = self.client.get(
            reverse('comment_delete', args=['test-post', self.comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comment_delete.html')

    def test_view_post_like(self):
        """
        Test for likes for posts
        """
        self.client.login(username='nameistest', password='passwordistest')
        likes = self.post.likes.count()
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(self.post.likes.count(), likes+1)
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(self.post.likes.count(), likes)

    def test_get_view_about(self):
        """
        Test to get About page and template about.html
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html', 'about.html')

    def test_get_view_category(self):
        """
        Test to get Category pages and template category.html
        """
        response = self.client.get(
            reverse('category', args=[self.category.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html', 'category.html')
