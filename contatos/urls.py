from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>', views.index, name="index"),
    path('login/', include('accounts.urls'), name="logina_index"),
    path('busca/<int:pk>', views.busca, name="busca"),
    path('contato/<int:contato_id>', views.ver_contato, name="ver_contato"),
    path('comment/<int:pk>', views.enviar_comentario, name="envia_coment"),
]