# Generated by Django 2.2.3 on 2020-10-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_contato_new_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='new_senha',
            field=models.CharField(blank=True, default='123456', max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='new_code',
            field=models.CharField(blank=True, default='dsadsadsadadgfdg', max_length=350),
        ),
    ]
