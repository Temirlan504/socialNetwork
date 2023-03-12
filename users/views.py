from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def profile_view(request):
    return render(request, "users/profile.html")

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