# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 05/02/2022
# Data do término: 05/02/2022
# Atividade 011: Letra B

# Crie uma função que receba uma lista de números. Depois retorne duas listas
# com os números pares, os números ímpares, a quantidade de números pares e
# quantidade de números ímpares.

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Função:


def cadastro_alunos():
    """[Função com estrutura de repetição para cadastro de 5 alunos]

    Returns:
     listaDeAlunos  [int]: [lista com os dict's dos alunos]
    """
    listaDeAlunos = []
    aluno = dict()
    for c in range(0, 5):
        aluno['Nome'] = str(input(f'{c+1}ª.Nome: '))
        aluno['Matricula'] = int(input(f'{c+1}ª.Matricula: '))
        aluno['Data'] = str(input(f'{c+1}ª.Data de nacimento: '))
        listaDeAlunos.append(aluno.copy())
        print()

    return listaDeAlunos


# Texto de entrada:
print('='*70)
print('INICIO DO PROGRAMA')
print('='*70)
print()

# Entrada de dados
print('Cadastro de alunos: ')
print()

# Invocando a função:
retorno = cadastro_alunos()
print()
print('-'*70)
print()

# Saida de dados:
print(f'A lista de alunos e: ')
print()

# Estrutura de repetição de saida de dados:
for i, c in enumerate(retorno): 
    for chave, valor in c.items():
        print(f'{chave}:    {valor}')
    print()
# Eu usei esse esquema para saida de dados de uma forma que ficou visualmente melhor, vamos la:
# Eu usei uma estrutura de repetição para varrer a lista com os dicionarios para separar elas por indicie e uma segunda para separar
# as chaves e valores do dicionario.
# [retorno] = E uma lista com varios dicionarios que veio do desempacotamento da função exemplo: [{dicionario 1}{dicionario2}{dicionario3}]     
# [ i ] = indicie do dicionario ou seja: [i1={dicionario 1}i2={dicionario2}i3={dicionario3}]
# [ c ] = são os dicionarios dentro da lista retorno
# [chave / valor in c.items() ] = são as chaves e valores do dicionario exemplo: [Nome: / Matricula: / Data: ]
# apos os prints das chaves e valores dentro de 1 dicionairo ou seja 3 chaves e 3 valores
# Eu uso um print para separar de um dicionario do outro, fora do segundo for (for in c.items()) 
# que esta dentro do primeiro for (for enumerate(retorno)) ou seja sempre vai dar um espaço a cada indicie ou seja cada dicionario.
# Resultado:
#A lista de alunos e:
#Nome:    Denilsom
#Matricula:    1
#Data:    1994
#
#Nome:    Vitor
#Matricula:    2
#Data:    2003
#
#Nome:    Delcio
#Matricula:    3
#Data:    1960
# Espero ter explicado e ajudado.

# Texto de encerramento:
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
