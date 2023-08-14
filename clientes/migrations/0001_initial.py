# Generated by Django 4.2.4 on 2023-08-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=9, verbose_name='RG')),
                ('celular', models.CharField(max_length=14, verbose_name='Celular')),
                ('ativo', models.BooleanField()),
            ],
        ),
    ]
