from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    # validando todos os campos 
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Numero de CPF invalido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O campo nome não pode ter numeros"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O numero do celular deve seguir este modelo 88 90088-0999 (respeitando os espaços e traço.)"})
        return data
    
    
    