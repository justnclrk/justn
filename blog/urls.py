from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, TagIndexView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('topic/<slug:slug>/', TagIndexView.as_view(), name='tagged'),
]
