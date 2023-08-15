import re


def cpf_valido(numero_do_cpf):
    ''' validando CPF para que ele tenha 11 digitos '''
    return len(numero_do_cpf) == 11

def nome_valido(nome):
    ''' validando NOME para que ele nao tenha numeros '''
    return nome.isalpha()

def rg_valido(numero_do_rg):
    ''' validando RG para que ele tenha 9 digitos '''
    return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
    ''' validando CELULAR para que ele tenha o formato de numero certo '''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_do_celular)
    return resposta
            