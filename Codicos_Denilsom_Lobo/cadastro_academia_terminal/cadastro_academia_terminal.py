# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data do ínicio: 06/02/2022
# Data do término: 06/02/2022
# Atividade 011: Letra H

# Uma Academia deseja fazer um senso entre seus clientes para descobrir a média
# de altura e peso de seus clientes. Faça um programa que pergunte a cada um 
# dos clientes da academia seu código, nome, altura e peso. Após esse 
# cadastramento, seu programa deverá listar os dados dos clientes e a média. 
# Para sair do programa o usuário deverá digitar o valor zero(0). O número de 
# clientes é indefinido. Sua saída deverá ser semelhante a ilustração ao lado:

# Importando as bibliotecas:
import os
from modulos_h.funcoes_h import *


# Limpando o terminal:
os.system('cls')


# declaração:
lista_chave = ['codico','nome','altura','peso']
lista_valores = []
lista_alunos = []
# Entrada de dados:
flag = True
while(True):
    print('PROGRAMA: ACADEMIA')
    print()
    print('-'*70)
    painel_academia()
    escolha = input('Escolha uma função: ')
    print()
    # Condicional de validação da escolha:
    if (not(escolha.isnumeric())) or (int(escolha)< 0 ) or (int(escolha) > 2):
        print('Digite apenas numeros inteiros de 0 a 2.')
        os.system('cls')
    else:
        escolha = int(escolha)
        print('-'*70)
        print(f'Você escolheu a função numero: {escolha}')
        print('-'*70)

    # Condicionais de escolha:

        # Escolha CADASTRO.
        if(escolha == 1):
            # Estrutura de repetição para entrada e saida da função.
            flag = True
            while(True):
                print('PROGRAMA: ACADEMIA')
                print()
                print('-'*70)
                print()
                print('CADASTRO')
                print('-'*70)
                print()
                desejo = str(input('Deseja cadastrar ? (s/n): ')).lower().strip()
                print()
                # Condicional de validação:
                if (desejo != 's') and (desejo != 'n'):
                    print('Entrada invalida ...')
                    print()
                else:
                    if(desejo == 'n'):
                        os.system('cls')
                        break
                    elif (desejo == 's'):
                    # Estrutura de repetição para repetir a função:                      
                        flag = True
                        while(True):
                            desejo = str(input('Deseja continuar cadastrando aluno ? (s/n): ')).lower().strip()
                            print()
                            # Condicional de validação:
                            if (desejo != 's') and (desejo != 'n'):
                                print('Entrada invalida ...')
                                print()
                            else:
                                if(desejo == 'n'):
                                    os.system('cls')
                                    break
                                elif (desejo == 's'):
                                    while(True):
                                        try:
                                            lista_valores.clear()
                                            print('-'*80)
                                            print()
                                            codico = int(input('Insira o códico: '))
                                            lista_valores.append(codico)
                                            print()
                                            nome = str(input('Insira o nome: '))
                                            lista_valores.append(nome)
                                            print()
                                            altura = float(input('Insira a altura: '))                               
                                            lista_valores.append(altura)
                                            print()
                                            peso = float(input('Insira o peso: '))                                    
                                            print()
                                            lista_valores.append(peso)
                                            # Invocando a função:
                                            novo_aluno = formador_Dict(lista_chave,lista_valores)
                                            print(f'Novo aluno e: {novo_aluno}')
                                            print()
                                            lista_alunos.append(novo_aluno.copy())
                                            
                                        except ValueError:
                                            print()
                                            print('ValueError: Você digitou uma entrada de valor errada')
                                            print_error_valor()
                                            print()
                                            print('Faça o cadastro novamente ...')
                                        break
                                        

        # Escolha LISTAR ALUNOS CADASTRADOS.
        if(escolha == 2):
            # Estrutura de repetição para entrada e saida da função.
            flag = True
            while(True):
                print('PROGRAMA: ACADEMIA')
                print()
                print('-'*70)
                print()
                print('LISTAR ALUNOS CADASTRADOS')
                print('-'*70)
                print()
                desejo = str(input('Deseja listar alunos cadastrados ? (s/n): ')).lower().strip()
                print()
                # Condicional de validação:
                if (desejo != 's') and (desejo != 'n'):
                    print('Entrada invalida ...')
                    print()
                else:
                    if(desejo == 'n'):
                        os.system('cls')
                        break
                    elif (desejo == 's'):
                    # Estrutura de repetição para repetir a função:                      
                        flag = True
                        while(True):
                            desejo = str(input('Continuar Listando alunos cadastrados ? (s/n): ')).lower().strip()
                            print()
                            # Condicional de validação:
                            if (desejo != 's') and (desejo != 'n'):
                                print('Entrada invalida ...')
                                print()
                            else:
                                if(desejo == 'n'):
                                    os.system('cls')
                                    break
                                elif (desejo == 's'):
                                     print('PROGRAMA: ACADEMIA')
                                     print()
                                     print('-'*70)
                                     print('Códico          Nome            Altura          Peso')
                                     print('='*70)
                                     #####
                                    
                                     for i, c in enumerate(lista_alunos):
                                         print()
                                         for valor in c.values():
                                             print(f'{valor}', end='\t\t')
                                     print()
                                     print()
                                     print('-'*70)
                                     # Invocando a função:
                                     media_alt, media_kg = media_altura_peso(lista_alunos)                                     
                                     print(f'Média:                         {media_alt:5.2f}         '+
                                     f'   {media_kg:5.2f}')
                                     print('='*70)
                                     print()

        # Escolha sair:
        elif (escolha == 0):
            print()
            print('-'*80)
            print('Saindo do PROGRAMA: ACADEMIA')
            print('-'*80)
            print()
            print('='*80)
            print('Fim do programa')
            print('='*80)
            break                 

# Considerações finais: Programa pode ser aprimorado ou programado de varias
# outras formas, porem feito com o intuito de mostrar algumas formas de utilizar 
# as funções em um programa.