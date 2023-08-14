from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    # validando CPF para que ele tenha 11 digitos
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 digitos')
        return cpf
    
    # validando NOME para que ele nao tenha numeros
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O campo nome não pode ter numeros')
        return nome
    
    # validando RG para que ele tenha 9 digitos
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError('O RG deve ter 9 digitos')
        return rg
    
    # validando CELULAR para que ele tenha 14 digitos
    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError('O CELULAR deve ter 11 digitos')
        return celular
    
    