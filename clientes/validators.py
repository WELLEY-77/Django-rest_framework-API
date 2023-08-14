# validando CPF para que ele tenha 11 digitos
def cpf_valido(numero_do_cpf):
    return len(numero_do_cpf) == 11

# validando NOME para que ele nao tenha numeros
def nome_valido(nome):
    return nome.isalpha()

# validando RG para que ele tenha 9 digitos
def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

# validando CELULAR para que ele tenha 14 digitos
def validate_celular(numero_do_celular):
    return len(numero_do_celular) < 11
            