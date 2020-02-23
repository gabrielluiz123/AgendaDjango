from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'categoria')
    list_display_links = ('id', 'nome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'email', 'sobrenome')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
