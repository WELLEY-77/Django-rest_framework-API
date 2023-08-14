from django.contrib import admin
from clientes.models import Cliente

class ClienteList(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'cpf', 'celular','ativo')
    list_display_links = ('id','nome', 'email', 'celular')
    search_fields = ('nome',)
    list_editable = ('ativo',)
    list_filter = ('ativo',)
    list_per_page = 10

admin.site.register(Cliente, ClienteList)
