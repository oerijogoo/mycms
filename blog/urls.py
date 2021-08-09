from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-index'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-blogs'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('post/new', PostCreateView.as_view(), name='blog-new'),
]

