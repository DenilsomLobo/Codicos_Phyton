# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data de início: 02/12/2021
# Data de término: 02/12/2021
# Atividade 009. Denilsom. Turma 11. Letra B.

# Programa de lista de compras

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declarações
listaRaiz = ('arroz', 'feijão', 'farofa', 'oleo', 'ovo', 'tempeiro')
listaAcressimo = []

# Texto de entrada
print('='*80)
print('LISTA DE COMPRAS')
print('='*80)
print()

# Estrutura de repetição para verificar lista:
while(True):
    # Validação de verificação:
    verTupla = str(input('Deseja ver a lista basica de '+
    'compra de todo mês ? (s/n): ')).lower().strip()
    print()
    if(verTupla != 's') and (verTupla != 'n'):
        print('Entrada invalida ...')
        print()
    # Condicionais de verificação:
    else:
        if(verTupla == 'n'):
            os.system('cls')
            break
        elif(verTupla == 's'):
            print()
            print(f'Está e a sua lista de compras que faz '+
            f'todo mês: {listaRaiz}')
            print() 

# Estrutura de repetição de entrada de dados na lista:
while(True):
    print('='*80)
    print('LISTA DE COMPRAS')
    print('='*80)
    print()
    # Entrada de dados:
    add = str(input('Insira o que vai comprar na lista '+
    ' ("p" = pular): ').lower().strip())
    print()
    # Condicional para pular:
    if (str(add) == 'p'):
        # Conversão de Tupla:
        listaRaiz = list(listaRaiz)
        listaRaiz.extend(listaAcressimo)
        listaRaiz = tuple(listaRaiz)
        os.system('cls')
        break
    # Condicional para validação de acressimo na lista:
    elif (True):
        # Acressimo de itens na lista.
        listaAcressimo.append(add)

    # Estrutura de repetição para validação e verificação da montagem de lista:
    while (True):
        print()
        # Entrada para validação e verificação da montagem da lista:
        sair = str(input('Se deseja continuar adicionando a lista use ("s")'+
        ' caso queira ver sua lista ate agora use ("n") para sair use ("p")'+
        'na hora de inserir: '))
        print()
        # Condicionais para validação e verificação da montagem da lista:
        if (sair != 's') and (sair != 'n'):
            print('Entrada invalida...')
            print() 
        elif (sair == 's'):
            os.system('cls')
            break
        elif (sair == 'n'):
            print('-'*80)
            print(f'Sua lista e : {listaAcressimo}')
            print('-'*80)

# Estrutura de repetição para verificação de itens na lista:
print('='*80)
print('LISTA DE COMPRAS')
print('='*80)
print()
while (True):
    # Entrada para verificação de itens na lista:
    comando = str(input('Deseja verificar se algum item '+
    'está na lista ? (s/n): '))
    print()
    # Validação:
    if (comando != 's') and (comando != 'n'):
        print('Entrada invalida ...')
        print()
    # Condicionais para a verficação de itens na lista:
    elif (comando == 's'):
        procurar = str(input('O que deseja procurar na lista? : '))
        print()
        if (procurar not in listaRaiz):
            print('Não esta na lista !')
            print()
        elif (procurar in listaRaiz):
            busca = listaRaiz.index(procurar)
            print()
            print(f'Ele está na lista na posição: {busca}')
            print()
    # Saida do laço:
    elif(comando == 'n'):
        os.system('cls')
        break

# Estrutura de repetição para verificação da quantidade de itens na lista:
print('='*80)
print('LISTA DE COMPRAS')
print('='*80)
print()
while (True):
    # Entrada para verificação de itens na lista:
    comando = str(input('Deseja verificar a quantidade de '+
    'algum item na lista ? (s/n): '))
    print()
    # Validação:
    if (comando != 's') and (comando != 'n'):
        print('Entrada invalida ...')
        print()
    # Condicionais para a verficação de itens na lista:
    elif (comando == 's'):
        quantidade = str(input('Qual item deseja procurar a '+
        'quantidade na lista? : '))
        print()
        if (quantidade not in listaRaiz):
            print('Não esta na lista !')
            print()
        elif (quantidade in listaRaiz):
            calcular = listaRaiz.count(quantidade)
            print(f'A quantidade de itens nessa lista é: {calcular}')
            print()
    # Saida do laço:
    elif(comando == 'n'):
        os.system('cls')
        break

# Sainda de dados da lista:
print('='*80)
print('LISTA DE COMPRAS')
print('='*80)
print()
print('ESTÁ E A SUA LISTA DE COMPRAS:')
print('-'*80)
# Estrutura de repetição de saida de dados:
for i, compras in enumerate(listaRaiz):
    print(f'No índice: {i} : {compras}')
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)


# Considerações finais: Programa pode ser aprimorado ou programado de varias
# outras formas, porem feito com o intuito de mostrar algumas formas de utilizar 
# as Tuplas e seus métodos em um programa.