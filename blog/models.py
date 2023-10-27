from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Published"))


# Category model
class Category(models.Model):
    """
    Models the fields for Post Categories.
    Can separate the views of the posts
    by category value.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


# Author Bio model
class AuthorBio(models.Model):
    """
    Model for the author bio field for a blog Post.
    """
    author_bio = models.CharField(max_length=600)

    def __str__(self):
        return self.author_bio


# Post model
class Post(models.Model):
    """
    Model of the fields for the blog Posts.
    """
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    author_bio = models.CharField(max_length=6000, default='author')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def read_time(self):
        return round(len(self.content.split(' ')) / 250)


# Comments
class Comment(models.Model):
    """
    Model for comments in Posts.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
