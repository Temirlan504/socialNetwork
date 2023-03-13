from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    # dispatch handles all the requests
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("users:login")
        return super().dispatch(request, *args, **kwargs)

    model = Post
    template_name = "newsfeed/main.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post