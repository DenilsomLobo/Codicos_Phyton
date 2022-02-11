# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 06/02/2022
# Data do término: 06/02/2022
# Atividade 011: Letra G

# Crie um programa que apresente ao usuário as seguintes operações:
# 1. Soma 2 . Subtração 3 . Produto 4 . Divisão 5. Divisão inteira 6 .
# Resto da divisão 7. Sair
# Escolhida a operação, peça também 2 números. Em seguida você criará
# funções que retorna o
# resultado das operações, imprimindo o resultado.

# Importando as bibliotecas:
import os
from modulos_g.funcoes_g import *

# Limpando o terminal:
os.system('cls')


# Estrutura de repetição de entrada de dados da escolha do painel 1 a 7:
flag = True
while (True):
    print('='*80)
    print_calculadora()
    print('='*80)
    painel_calculadora()
    escolha = input('Digite o numero: ')
    print()
    # Condicional de validação da escolha:
    if (not(escolha.isnumeric())) or (int(escolha) < 1) or (int(escolha) > 7):
        print('Digite apenas numeros inteiros de 1 a 7.')
        os.system('cls')
    else:
        escolha = int(escolha)
        print('-'*70)
        print(f'Você escolheu a função numero: {escolha}')
        print('-'*70)

    # Condicionais de escolha:

        # Escolha somar.
        if(escolha == 1):
            # Estrutura de repetição para entrada e saida da função.
            flag = True
            while(True):
                print('-'*70)
                print('Função somar: ')
                print('-'*70)
                desejo = str(
                    input('Deseja continuar na função somar ? (s/n): ')).lower().strip()
                # Condicional de validação:
                if (desejo != 's') and (desejo != 'n'):
                    print('Entrada invalida ...')
                    print()
                else:
                    if(desejo == 'n'):
                        os.system('cls')
                        break

                    elif (desejo == 's'):
                        print('-'*80)
                        print()
                        while(True):
                            try:
                                valor_a = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        while(True):
                                try:
                                    valor_b = float(input('Insira o primeiro valor: '))
                                    break
                                except ValueError:                                
                                    print('Erro de entrada de valor !')
                                    print()
                        print()
                        print('-'*80)
                        print()
                        retorno = somar(valor_a, valor_b)
                        print(retorno)
                        print()
                        print('='*80)

        # Escolha subtração :
        elif (escolha == 2):
            # Estrutura de repetição para entrada e saida da função.
            flag = True
            while(True):
                print('-'*70)
                print('Função subtrair: ')
                print('-'*70)
                desejo = str(
                    input('Deseja continuar na função subtrair ? (s/n): ')).lower().strip()
                # Condicional de validação:
                if (desejo != 's') and (desejo != 'n'):
                    print('Entrada invalida ...')
                    print()
                else:
                    if(desejo == 'n'):
                        os.system('cls')
                        break
                    else:
                        if(desejo == 'n'):
                            os.system('cls')
                            break
                        elif (desejo == 's'):
                            print('-'*80)
                            print()
                            while(True):
                                try:
                                    valor_a = float(input('Insira o primeiro valor: '))
                                    break
                                except ValueError:                                
                                    print('Erro de entrada de valor !')
                                    print()
                            print()
                            while(True):
                                try:
                                    valor_b = float(input('Insira o primeiro valor: '))
                                    break
                                except ValueError:                                
                                    print('Erro de entrada de valor !')
                                    print()
                            print('-'*80)
                            print()
                            retorno = subtrair(valor_a, valor_b)
                            print(retorno)
                            print()
                            print('='*80)

        # Escolha produto:
        elif (escolha == 3):
            # Estrutura de repetição para entrada e saida da função.
            flag = True
            while(True):
                print('-'*70)
                print('Função produto: ')
                print('-'*70)
                desejo = str(
                    input('Deseja continuar na função produto ? (s/n): ')).lower().strip()
                # Condicional de validação:
                if (desejo != 's') and (desejo != 'n'):
                    print('Entrada invalida ...')
                    print()
                else:
                    if(desejo == 'n'):
                        os.system('cls')
                        break
                    elif (desejo == 's'):
                        print('-'*80)
                        print()
                        while(True):
                            try:
                                valor_a = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        while(True):
                            try:
                                valor_b = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        print('-'*80)
                        print()
                        retorno = produto_calcular(valor_a, valor_b)
                        print(retorno)
                        print()
                        print('='*80)

        # Escolha divisão:
        elif (escolha == 4):
            # Estrutura de repetição para entrada e saida da função.
            flag = True
            while(True):
                print('-'*70)
                print('Função divisão: ')
                print('-'*70)
                desejo = str(
                    input('Deseja continuar na função divisão ? (s/n): ')).lower().strip()
                # Condicional de validação:
                if (desejo != 's') and (desejo != 'n'):
                    print('Entrada invalida ...')
                    print()
                else:
                    if(desejo == 'n'):
                        os.system('cls')
                        break
                    elif (desejo == 's'):
                        print('-'*80)
                        print()
                        while(True):
                            try:
                                valor_a = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        while(True):
                            try:
                                valor_b = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        print('-'*80)
                        print()
                        retorno = dividir(valor_a, valor_b)
                        print(retorno)
                        print()
                        print('='*80)

        # Escolha divisão inteira:
        elif (escolha == 5):
            # Estrutura de repetição para entrada e saida da função.
            flag = True
            while(True):
                print('-'*70)
                print('Função divisão inteira: ')
                print('-'*70)
                desejo = str(
                    input('Deseja continuar na função divisão inteira ? (s/n): ')).lower().strip()
                # Condicional de validação:
                if (desejo != 's') and (desejo != 'n'):
                    print('Entrada invalida ...')
                    print()
                else:
                    if(desejo == 'n'):
                        os.system('cls')
                        break

                    elif (desejo == 's'):
                        print('-'*80)
                        print()
                        while(True):
                            try:
                                valor_a = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        while(True):
                            try:
                                valor_b = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        print('-'*80)
                        print()                        
                        retorno = divisao_inteira(valor_a, valor_b)
                        print(retorno)
                        print()
                        print('='*80)

        # Escolha resto da divisão:
        elif (escolha == 6):
            # Estrutura de repetição para entrada e saida da função.
            flag = True
            while(True):
                print('-'*70)
                print('Função resto da divisão: ')
                print('-'*70)
                desejo = str(
                    input('Deseja continuar na função resto da divisão ? (s/n): ')).lower().strip()
                # Condicional de validação:
                if (desejo != 's') and (desejo != 'n'):
                    print('Entrada invalida ...')
                    print()
                else:
                    if(desejo == 'n'):
                        os.system('cls')
                        break
                    elif (desejo == 's'):
                        print('-'*80)
                        print()
                        while(True):
                            try:
                                valor_a = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        while(True):
                            try:
                                valor_b = float(input('Insira o primeiro valor: '))
                                break
                            except ValueError:                                
                                print('Erro de entrada de valor !')
                                print()
                        print()
                        print('-'*80)
                        print()
                        retorno = divisao_resto(valor_a, valor_b)
                        print(retorno)
                        print()
                        print('='*80)

        # Escolha sair:
        elif (escolha == 7):
            print()
            print('-'*80)
            print('Obrigado por ter usado meu programa')
            print('-'*80)
            print_saida()
            print()
            print('='*80)
            print('Fim do programa')
            print('='*80)
            break

# Considerações finais: Programa pode ser aprimorado ou programado de varias
# outras formas, porem feito com o intuito de mostrar algumas formas de utilizar
# as funções em um programa.
