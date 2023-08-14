from django.shortcuts import render
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from rest_framework import viewsets


class ClientesViewSet(viewsets.ModelViewSet):
    ''' Listando todos os clientes '''

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 