# Generated by Django 2.2.3 on 2020-10-04 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0007_remove_contato_new_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='new_code',
        ),
    ]