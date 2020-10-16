from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/<int:pk>', views.login, name='login'),
    path('logout/<int:pk>', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/<int:pk>', views.dashboard, name='dashboard'),
]