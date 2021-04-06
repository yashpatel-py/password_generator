from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password_generate/', views.password_generate, name='password_generate'),
]