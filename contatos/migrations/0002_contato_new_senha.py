# Generated by Django 2.2.3 on 2020-10-06 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='new_header',
            field=models.CharField(blank=True, default=' ', max_length=350, null=True),
        ),
    ]
