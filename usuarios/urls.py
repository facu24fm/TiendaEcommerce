from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registro, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
]
