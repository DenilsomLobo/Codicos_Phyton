# Funções:
from decimal import DivisionByZero
from logging import exception


def print_calculadora():
    """ [Função que printa ARTCII= calculadora]
     """
    print("""
                  888                   888               888                          
                  888                   888               888                          
                  888                   888               888                          
 .d8888b  8888b.  888  .d8888b 888  888 888  8888b.   .d88888  .d88b.  888d888 8888b.  
d88P"        "88b 888 d88P"    888  888 888     "88b d88" 888 d88""88b 888P"      "88b 
888      .d888888 888 888      888  888 888 .d888888 888  888 888  888 888    .d888888 
Y88b.    888  888 888 Y88b.    Y88b 888 888 888  888 Y88b 888 Y88..88P 888    888  888 
 "Y8888P "Y888888 888  "Y8888P  "Y88888 888 "Y888888  "Y88888  "Y88P"  888    "Y888888
""")


def painel_calculadora():
    """ [Função que printa ARTCII= painel calculadora]
     """    
    print("""
     ____________________________________________   
    | Digite um numero para definir uma função   |
    | para calculadora :                         |
    |                                            |
    | 1 = SOMA              4 = DIVISÃO          |               
    | 2 = SUBTRAÇÃO         5 = DIVISÃO INTEIRA  |
    | 3 = PRODUTO           6 = RESTO DA DIVISÃO |
    |                                            |
    |               7 = SAIR                     |
    |____________________________________________|
    """)

def print_saida():
    """ [Função que printa ARTCII= função que printa imagem de saida]
     """
    print("""
████████████████████████████████████████
████████████████████████████████████████
██████▀░░░░░░░░▀████████▀▀░░░░░░░▀██████
████▀░░░░░░░░░░░░▀████▀░░░░░░░░░░░░▀████
██▀░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░░▀██
██░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░▄▀░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░████▄▄▄▀░░▀▀▀▀▄░░░░░░░░░░░██
██▄░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░▄██
████▄░░░░░░░████░░░░░░░░░░█░░░░░░░░▄████
██████▄░░░░░████▄▄▄░░░░░░░█░░░░░░▄██████
████████▄░░░▀▀▀▀░░░▀▀▀▀▀▀▀░░░░░▄████████
██████████▄░░░░░░░░░░░░░░░░░░▄██████████
████████████▄░░░░░░░░░░░░░░▄████████████
██████████████▄░░░░░░░░░░▄██████████████
████████████████▄░░░░░░▄████████████████
██████████████████▄▄▄▄██████████████████
████████████████████████████████████████
████████████████████████████████████████

    """)

def somar(a, b):
    """[Função que faz a soma de A + B]

    Args:
        a ([float]): [valor1]
        b ([float]): [valor2]
    """
    s = a + b
    return f'A soma de {a} + {b}  = {s} '

def subtrair(a, b):
    """[Função que faz a subtrair de A + B]

    Args:
        a ([float]): [valor1]
        b ([float]): [valor2]
    """
    s = a - b
    return f'A subtração de {a} - {b} = {s}'

def produto_calcular(a, b):
    """[Função que faz o produto de A + B]

    Args:
        a ([float]): [valor1]
        b ([float]): [valor2]
    """
    s = a * b
    return f'O produto de {a} X {b} = {s}'

def dividir(a, b):
    """[Função que faz a dividir de A + B]

    Args:
        a ([float]): [valor1]
        b ([float]): [valor2]
    """
    try:
        s = a / b
        return f'A divisão de {a} ÷ {b} = {s} '

    except ZeroDivisionError:
        return print('ERRO! Não podemos dividir um número por zero!')
    
    

def divisao_inteira(a, b):
    """[Função que faz a divisão de inteiros de A + B]

    Args:
        a ([float]): [valor1]
        b ([float]): [valor2]
    """
    try:
        s = a // b
        return f'A divisão inteira de {a} // {b} = {s}'

    except ZeroDivisionError:
        return 'ERRO! Não podemos dividir um número por zero!'

    

def divisao_resto(a, b):
    """[Função que faz o resto da divisão de A + B]

    Args:
        a ([float]): [valor1]
        b ([float]): [valor2]
    """
    try:
        s = a % b
        return f'O resto da divisão de {a} % {b} = {s}'

    except ZeroDivisionError:
        return 'ERROR! Não podemos dividir um número por zero!'