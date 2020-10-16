import ast

from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pymysql.cursors
import cgitb
from django.utils.html import escape

conexao = pymysql.connect(
    host='18.219.154.84',
    user='admin',
    password='Maria@1601',
    db='sitedjango',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conexao.cursor()

@login_required(redirect_field_name='logina_index')
def index(request, *args, **kwargs):
    pk_desafio = kwargs.get('pk')
    contatos = Contato.objects.order_by('-nome').filter(
        desafio_id=pk_desafio
    )
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos,
        'desafio_id': pk_desafio,
    })


@login_required(redirect_field_name='logina_index')
def busca(request, *args, **kwargs):
    pk_desafio = kwargs.get('pk')
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'O campo não pode ser vazio!')
        return redirect('index')
    campos = Concat('nome', Value(' '), 'sobrenome')

    # contatos = Contato.objects.order_by('-nome').filter(
    # Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
    #  mostrar=True
    # )

    try:
        cursor = conexao.cursor()
        cursor.execute(f'SELECT new_code FROM contatos_contato WHERE desafio_id = {pk_desafio}')
        resultado1 = cursor.fetchall()


        for resultado in resultado1:
            print(resultado)
            for key in resultado:
                resultado_code = resultado[key] = resultado[key]
                print('Try')
        print(resultado_code)
        contatos = eval(resultado_code)
        print('EXECUTADO')
        cursor.close()
    except:
        print('Except')
        termo = termo.split(';')
        cursor = conexao.cursor()
        cursor.execute(f'{termo[1]}')
        contatos = Contato.objects.raw(f'SELECT * FROM contatos_contato WHERE nome LIKE "{termo[0]}"')
        conexao.commit()
        cursor.close()
    # contatos = Contato.objects.annotate(
    # nome_completo=campos
    # ).filter(
    #  Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
    #  mostrar=True
    # )


    return render(request, 'contatos/busca.html', {
        'contatos': contatos,
        'desafio_id':pk_desafio
    })


@login_required(redirect_field_name='logina_index')
def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    contato_d = contato.desafio_id

    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato,
        'desafio_id': contato_d
    })

@login_required(redirect_field_name='logina_index')
def enviar_comentario(request, *args, **kwargs):
    pk_desafio = kwargs.get('pk')
    # contato = Contato.objects.get(id=contato_id)
    contato = Contato.objects.get(desafio_id=pk_desafio)
    contato_d = contato.desafio_id
    try:
        cursor = conexao.cursor()
        cursor.execute(f'SELECT new_header, id FROM contatos_contato WHERE desafio_id = {pk_desafio}')
        cursor.close()
        resultado1 = cursor.fetchall()

        for resultado in resultado1:
            for key in resultado:
                resultado_usuario = resultado['new_header']
                print(resultado['id'])
                print('Try')
        print(resultado_usuario)
        comentario = eval(resultado_usuario)
    except:
        comentario = request.POST.get('comment')
    contato.new_header2 = comentario
    contato.save()
    comentario2 = contato.new_header2
    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato,
        'desafio_id': contato_d,
        'comentario': comentario2
    })
