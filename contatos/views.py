from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='logina_index')
def index(request):
    contatos = Contato.objects.order_by('-nome').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

@login_required(redirect_field_name='logina_index')
def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'O campo não pode ser vazio!')
        return redirect('index')
    campos = Concat('nome', Value(' '), 'sobrenome')
    #contatos = Contato.objects.order_by('-nome').filter(
      #  Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
      #  mostrar=True
    #)
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True
    )
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })

@login_required(redirect_field_name='logina_index')
def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/ver_contato.html', {
         'contato': contato
    })
