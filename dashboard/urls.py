from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('login/', views.Login, name='login'),
	path('register/', views.Register, name='register'),
]