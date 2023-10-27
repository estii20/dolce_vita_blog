from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category, AuthorBio
from .forms import CommentForm, PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class PostList(generic.ListView):
    """
    Displays page view of blog post.
    Additional options to add a like or comment.
    Access to all options dependent on login status.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    Display view for individual blog posts on one page,
    options are to add a comment or like a post.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Get method to retrieve post details including comments and likes
        and render post detail page.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "author_bio": post
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post method validates comment input, save comment and then re-load
        the post detail page.
        Success message feedback for the user.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "author_bio": post
            },
        )


class PostLike(View):
    """
    View on post detail page to remove or add like.
    """

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    View to allow validated users to add a a new blog post.
    Success message feedback to the user.
    """
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    success_message = "Post was created successfully"


class EditPost(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    """
    View to allow validated users to edit their blog post
    on the post detail page.
    Success message feedback to user.
    """
    model = Post
    template_name = 'post_edit.html'
    form_class = PostForm
    success_message = "Post was edited successfully"

    def form_valid(self, form):
        """ Validate form after connecting form author to user """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Test that logged in user is post author """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    """
    View to allow validated users to delete their blog post
    on the post detail page.
    Success message feedback to the user.
    """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Post was deleted successfully"

    def test_func(self):
        """ Test that logged in user is post author """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CategoryView(View):
    """
    View to display Category page dependent on user choice.
    Requests list of posts with matching category.
    Renders view of the category.html template.
    """
    def get(self, request, category, *args, **kwargs):
        """ Gets posts filtered by category """
        queryset = Category.objects.all()
        category = get_object_or_404(self.queryset, category=category)
        posts = category.filter(status=1).order_by("-created_on")
        paginate_by = 6
        template_name = 'category.html'

        return render(
            request,
            'category.html',
            {'category': category,
             'posts': posts},
        )


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    """
    View to allow validated users to delete their comment
    on the post detail page.
    Success message feedback to the user.
    """
    model = Comment
    template_name = 'comment_delete.html'
    success_message = "Comment was deleted successfully"

    def get_success_url(self):
        """ Success url for comment with assciated comment """
        slug = self.kwargs['slug']
        return reverse_lazy('post_detail', kwargs={'slug': slug})

    def delete(self, request, *args, **kwargs):
        """ Success message on delete view """
        return super(CommentDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        """ Test that logged in user is comment user """
        comment = self.get_object()
        if self.request.user == comment.name:
            return True
        return False


class AboutView(generic.CreateView):
    """
    View for About page.
    Requests template by template name.
    Renders the view of about.html.
    """
    model = Post
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


def handler404(request, exception):
    """
    404 page for errors
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, "500.html", status=500)


def handler403(request, exception):
    """
    Custom 403 page
    """
    return render(request, "403.html", status=403)


def handler405(request, exception):
    """
    Custom 405 page
    """
    return render(request, "405.html", status=405)
