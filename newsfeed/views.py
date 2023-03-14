from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import (ListView, 
                                  DetailView, 
                                  UpdateView, 
                                  DeleteView, 
                                  CreateView)

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

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "newsfeed/post_create.html"
    success_url = reverse_lazy('newsfeed:main')

    # To connect author of the post to the user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "newsfeed/post_update.html"

    def get_success_url(self):
        return reverse_lazy('newsfeed:post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = "newsfeed/post_delete.html"
    success_url = reverse_lazy('newsfeed:main')