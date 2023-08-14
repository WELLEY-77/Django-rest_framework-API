from django.contrib import admin

class ClientesList(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'celular')
    list_display_links = ('nome', 'email', 'celular')
    list_editable = ('ativo',)
    list_filter = ('ativo',)
    list_per_page = 10
    search_fields = 'nome'
