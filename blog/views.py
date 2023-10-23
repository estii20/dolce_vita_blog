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
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
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

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    success_message = "Post was created successfully"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class EditPost(LoginRequiredMixin, 
                UserPassesTestMixin, 
                SuccessMessageMixin, 
                generic.UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostForm
    success_message = "Post was edited successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, 
                    UserPassesTestMixin, 
                    SuccessMessageMixin, 
                    generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Post was deleted successfully"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CategoryView(generic.ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category_name=self.kwargs['category']).order_by("-created_on")
        }

        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        'category_list': category_list,
    }

    return context


class CommentDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        generic.DeleteView):

    model = Comment
    template_name = 'comment_delete.html'
    success_message = "Comment was deleted successfully"

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('post_detail', kwargs={'slug': slug})
    
    def delete(self, request, *args, **kwargs):
        return super(CommentDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        comment = self.get_object()
        if self.request.username == comment.username:
            return True
        return False


def about_view(request, View):
    return render(request, 'blog/about.html')