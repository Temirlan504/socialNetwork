from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView
from newsfeed.models import Post

class UserPostListView(ListView):
    model = Post
    template_name = "users/profile.html"
    context_object_name = "posts"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        context['profile_user'] = user
        return context

def profile_update_view(request, username):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user) # "instance=" fills forms
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(reverse("users:profile", args=[request.user.username]))
    else:
        u_form = UserUpdateForm(instance=request.user) # "instance=" fills forms
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "users/profile_update.html", {
        "u_form": u_form,
        "p_form": p_form,
        "username": request.user.username
    })


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("newsfeed:main")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {
        "form": form,
        "title": "Register"
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("newsfeed:main")
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials",
                "title": "Login"
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out",
        "title": "Login"
    })