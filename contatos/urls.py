from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', include('accounts.urls'), name="logina_index"),
    path('busca/', views.busca, name="busca"),
    path('<int:contato_id>', views.ver_contato, name="ver_contato"),
]