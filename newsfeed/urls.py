from django.urls import path
from . import views
from .views import PostListView, PostDetailView

app_name = "newsfeed"

urlpatterns = [
    path('', PostListView.as_view(), name="main"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail")
]