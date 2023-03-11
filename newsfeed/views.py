from django.shortcuts import render, redirect
from .models import Post

def main(request):
    if not request.user.is_authenticated:
        return redirect("users:login")
     
    return render(request, "newsfeed/main.html", {
        "posts": Post.objects.all()
    })