from django.shortcuts import render
from .models import Post

def main(request):
    return render(request, "newsfeed/main.html", {
        "posts": Post.objects.all()
    })