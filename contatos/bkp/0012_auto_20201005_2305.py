# Generated by Django 2.2.3 on 2020-10-06 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0011_remove_contato_new_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='new_code',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='new_header',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='sql_desafio',
        ),
    ]
