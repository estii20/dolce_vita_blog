from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category, AuthorBio
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
        Post method validates comment input, save comment and then returns to
        the post detail page.
        """
        if request.user.is_authenticated:
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.name = request.user
                comment.save()
                messages.success(request, 'Thank you for your comment \
                    - Comment will be published shortly')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(LoginRequiredMixin, View):
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


class EditPost(LoginRequiredMixin,
               UserPassesTestMixin,
               SuccessMessageMixin,
               generic.UpdateView):
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


class DeletePost(LoginRequiredMixin,
                 UserPassesTestMixin,
                 generic.DeleteView):
    """
    View to allow validated users to delete their blog post
    on the post detail page.
    Success message feedback to the user.
    """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        """ Test that logged in user is post author """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        """ Overrides the delete function message to display success message"""
        messages.success(self.request, 'Post was successfully deleted')
        return super().delete(request, *args, **kwargs)


class CategoryView(generic.ListView):
    """
    View to display Category page dependent on user choice.
    Requests list of posts with matching category.
    Renders view of the category.html template.
    """
    model = Post
    template_name = 'category.html'

    def get(self, request, category, *args, **kwargs):
        """ Gets posts filtered by category """
        category_list = Category.objects.all()
        category = get_object_or_404(category_list, name=category)
        category_posts = Post.objects.filter(
            category=category).order_by("-created_on")

        # Number of items per page
        items_per_page = 6

        paginator = Paginator(category_posts, items_per_page)
        page = request.GET.get('page')

        try:
            categories = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer
            categories = paginator.page(1)
        except EmptyPage:
            # If page is not in range
            categories = paginator.page(paginator.num_pages)

        return render(
            request,
            self.template_name,
            {'category': category,
             'category_posts': categories},
        )


class CommentDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        generic.DeleteView):
    """
    View to allow validated users to delete their comment
    on the post detail page.
    Success message feedback to the user.
    """
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('home')

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

    def delete(self, request, *args, **kwargs):
        """ Overrides the delete function message to display success message"""
        messages.success(self.request, 'Comment was successfully deleted')
        return super().delete(request, *args, **kwargs)


class CommentEdit(LoginRequiredMixin,
                  UserPassesTestMixin,
                  SuccessMessageMixin,
                  generic.UpdateView):
    """
    View to allow validated users to edit their comment
    on the post detail page.
    Success message feedback to the user.
    """
    model = Comment
    template_name = 'comment_edit.html'
    form_class = CommentForm
    success_message = 'Comment successfully edited'

    def get_success_url(self):
        """ Success url for comment with assciated comment """
        slug = self.kwargs['slug']
        return reverse_lazy('post_detail', kwargs={'slug': slug})

    def form_valid(self, form):
        """Validate form after connecting form name of user to loggedin user"""
        form.instance.name = self.request.user
        return super().form_valid(form)

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
