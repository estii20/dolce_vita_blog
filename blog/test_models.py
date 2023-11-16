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

        # Create a post for testing
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

        # Create a comment for testing
        self.comment = Comment.objects.create(
            post=self.post,
            name=self.user,
            body='test comment'
        )

    def test_category_model(self):
        """
        Test Category model
        """
        # test post has a category
        category = Category.objects.get(name=1)
        self.assertEqual(str(category), '1')

        # test post is in correct post category
        self.assertEqual(self.post.category, self.category)

    def test_author_bio_model(self):
        """
        Test AuthorBio model
        """
        # test author_bio field content
        author_bio = AuthorBio.objects.get(author_bio='Test Author Bio')
        self.assertEqual(str(author_bio), 'Test Author Bio')

        # test post if multiple author bios added
        author_bio = AuthorBio.objects.create(
            author_bio='Multiple Author Bios')
        self.assertEqual(str(author_bio), 'Multiple Author Bios')

    def test_post_model(self):
        """
        Test Post model
        """
        # test post string
        post = Post.objects.get(title='Test Post')
        self.assertEqual(str(post), 'Test Post')
        # test post likes
        self.assertEqual(post.number_of_likes(), 0)
        # test post approved
        self.assertTrue(self.post.status == 1)
        # test post title string
        self.assertEqual(self.post.__str__(), self.post.title)
        # test post absolute url
        self.assertEqual(self.post.get_absolute_url(),
                         f'/post/{self.post.slug}/')
        # test post update title
        self.post.title = 'Update Test Post Title'
        # test save post
        self.post.save()
        # test update post title and update post slug
        self.assertEqual(self.post.slug, 'update-test-post-title')

    def test_post_title_maximum_length(self):
        """
        Test maximum length of a post
        """
        Post.objects.create(title='A' * 300,
                            slug='test-post',
                            author=self.user,
                            category_id=1)

    def test_comment_model(self):
        """
        Test Comment model
        """
        comment = Comment.objects.create(
            post=self.post,
            name=self.user,
            body='Test comment body',
            approved=True
        )
        # test comment body by comment user name
        self.assertEqual(
            str(comment), f'Comment Test comment body by {self.user}')
        # test comment approved field
        self.assertFalse(self.comment.approved)
        # test comment is for correct post
        self.assertEqual(self.comment.post, self.post)
        # test comment user is comment name
        self.assertEqual(self.comment.name, self.user)

    def test_comment_ordering(self):
        """
        Test to add a second comment and comment order
        """
        comment_2 = Comment.objects.create(
            post=self.post,
            name=self.user,
            body='Test comment body two',
            approved=True
        )

        comments = Comment.objects.filter(post=self.post)
        self.assertEqual(comments.first(), self.comment)
        self.assertEqual(comments.last(), comment_2)
