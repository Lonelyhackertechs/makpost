from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    PostListAPIView,
    PostDetailAPIView,
    CommentListCreateAPIView,
    CommentDetailAPIView,
    MyProfileView,
    LogoutView  # <- Add this
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # <- JWT logout endpoint

    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),

    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),

    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
]
