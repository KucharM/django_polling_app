from django.urls import path, include 
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserCreateView

app_name = 'users'

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]