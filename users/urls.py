from django.urls import path
from . import views
from .views import UserPostListView

app_name = "users"

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('<str:username>/', UserPostListView.as_view(), name="profile"),
    path('profile_update/<str:username>/', views.profile_update_view, name="profile_update")
]