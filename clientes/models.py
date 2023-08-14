from django.db import models

class Clientes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', blank=False, max_length=30)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    rg = models.CharField('RG', max_length=9)
    celular = models.CharField('Celular', max_length=14)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome