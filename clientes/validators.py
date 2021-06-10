import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome):
    nome = nome.strip()
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(numero_celular):
    """Verifica se o celular é válido (11 94525-1234)"""
    modelo = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    resposta = re.findall(modelo, numero_celular)
    return resposta

