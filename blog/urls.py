from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/edit/', views.EditPost.as_view(),
         name='post_edit'),
    path('<slug:slug>/delete/', views.DeletePost.as_view(),
         name='post_delete'),
    path('<slug:slug>/comment_delete/<int:pk>/', views.CommentDeleteView.as_view(),
         name='comment_delete'),
    path('<slug:slug>/comment_edit/<int:pk>', views.CommentEdit.as_view(),
         name='comment_edit'),
    path('category/<category>/', views.CategoryView.as_view(),
         name='category'),
    path('about/', views.AboutView.as_view(), name='about'),
]
