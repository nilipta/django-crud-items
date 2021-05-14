from django.urls import path
from . import views

urlpatterns = [
    path('', views.authPage, name='authHome'),
    path('login', views.loginForm, name='login'),
    path('signup', views.signup, name='signup')
]