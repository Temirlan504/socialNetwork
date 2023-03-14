from django.urls import path
# from . import views
from .views import (PostListView, 
                    PostDetailView, 
                    PostUpdateView, 
                    PostDeleteView,
                    PostCreateView)

app_name = "newsfeed"

urlpatterns = [
    path('', PostListView.as_view(), name="main"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('post/create/', PostCreateView.as_view(), name="post_create")
]