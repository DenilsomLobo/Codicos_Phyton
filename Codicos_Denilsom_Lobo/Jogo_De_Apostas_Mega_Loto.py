# Curso Tecnico de informatica
# Autor: Denilsom Lobo de Souza
# Data de inicio: 28/11/2021
# Data de termino: 28/11/2021
# Atividade 008: Letra N

# Programa que sorteia numeros da Mega Sena e da lotofácil.

# Importando as bibliotecas:
import os
import copy
from random import randint

# Limpando o terminal:
os.system('cls')

# Entrada de dados:
apostaMega = []
apostaLoto = []

# Texto de entrada:
print('='*80)
print('INICIO DO PROGRAMA')
print('='*80)

# Etrutura de repetição da entrada da aposta mega sena:
for c in range (0, 6):
    while (True):
        megaAdd = input('Digite os numeros que você quer apostar: ')
        if(not(megaAdd.isnumeric()) or int(megaAdd) < 0 or int(megaAdd) > 60):
            print()
            print(f'Entrada inválida, digite novamente ...')
            print()
        else:
            megaAdd = int(megaAdd)
            if megaAdd in apostaMega:
                print('Este numero ja foi apostado ...')
                continue
            elif megaAdd not in apostaMega:
                apostaMega.append(megaAdd)
                break      
# Etrutura de repetição da entrada da aposta mega sena:
print('-'*80)
print('Agora vamos apostar a Loto facil:')
print('-'*80)
for c2 in range (0, 15):
    while (True):
        lotoAdd = input('Digite os numeros que você quer apostar: ')
        if(not(lotoAdd.isnumeric()) or int(lotoAdd) < 0 or int(lotoAdd) > 25):
            print()
            print(f'Entrada inválida, digite novamente ...')
            print()
        else:
            lotoAdd = int(lotoAdd)
            if lotoAdd in apostaLoto:
                print('Este numero ja foi apostado ...')
                continue
            elif lotoAdd not in apostaLoto:
                apostaLoto.append(lotoAdd)
                break      
# Declaração:
listaDeNumerosMega = []
listaDeLotofacil = []

# Estrutura de repetição de numeros aleatorios:
# Mega Sena:
for c3 in range (0, 6):
    # Validações de numeros repetidos:
    while (True):
        numerosAleatoriosMega = randint (0, 60)
        if numerosAleatoriosMega in listaDeNumerosMega:
            continue
        else:
            numerosAleatoriosMega not in listaDeNumerosMega
            listaDeNumerosMega.append(numerosAleatoriosMega)
            break
# Lotofácil:     
for c4 in range (0, 15):
    # Validações de numeros repetidos:
    while (True):
        numerosAleatoriosLoto = randint (0, 25)
        if numerosAleatoriosLoto  in listaDeLotofacil:
            continue
        else:
            numerosAleatoriosLoto not in listaDeLotofacil
            listaDeLotofacil.append(numerosAleatoriosLoto)
            break
         
# Fatiamento de listas
listaCopiada = copy.copy(listaDeNumerosMega)
listaCopiada2 = copy.copy(listaDeLotofacil)
listaCrescenteMega = sorted(listaCopiada)
listaCrescenteLoto = sorted(listaCopiada2)
megasena = listaCrescenteMega [0: ]
lotofacil = listaCrescenteLoto [0: ]

# Texto de saida:
print('='*80)
print('O RESULTADO DO SORTEIO DA MEGA SENA FOI !!!')
print('='*80)
print()
print(f'Os numeros da Mega sena sorteados foi: {listaDeNumerosMega}')
print()
print(f'Anote os numeros: {megasena}')
print()
print('-'*80)
print()
print(f'Os numeros da Lotofácil sorteados foi: {listaDeLotofacil}')
print()
print(f'Anote os numeros: {lotofacil}')
print()
print('='*80)
print()
print(f'Sua aposta foi da mega sena foi:{apostaMega}')
print()
print()
print(f'Sua aposta da lotofácil foi: {apostaLoto}')
# Futuramente uma verificação de quantos numeros acertou e se ganhou ou não.
# Declarações de correção Mega Sena:
apostaMega01 = apostaMega [0]
apostaMega02 = apostaMega [1]
apostaMega03 = apostaMega [2]
apostaMega04 = apostaMega [3]
apostaMega05 = apostaMega [4]
apostaMega06 = apostaMega [5]
acertosMega = 0

# Condicionais de verificação:
if apostaMega01 in megasena:
    acertosMega += 1
elif apostaMega02 in megasena:
    acertosMega += 1
elif apostaMega03 in megasena:
    acertosMega += 1
elif apostaMega04 in megasena:
    acertosMega += 1
elif apostaMega05 in megasena:
    acertosMega += 1
elif apostaMega06 in megasena:
    acertosMega += 1
else:
    acertosMega += 0

print('-'*80)
print(f'A sua quantidade de acertos na mega sena foi: {acertosMega}')
print()
# Declarações de correções da Lotofácil:
apostaLoto01 = apostaLoto [0]
apostaLoto02 = apostaLoto [1]
apostaLoto03 = apostaLoto [2]
apostaLoto04 = apostaLoto [3]
apostaLoto05 = apostaLoto [4]
apostaLoto06 = apostaLoto [5]
apostaLoto07 = apostaLoto [6]
apostaLoto08 = apostaLoto [7]
apostaLoto09 = apostaLoto [8]
apostaLoto10 = apostaLoto [9]
apostaLoto11 = apostaLoto [10]
apostaLoto12 = apostaLoto [11]
apostaLoto13 = apostaLoto [12]
apostaLoto14 = apostaLoto [13]
apostaLoto15 = apostaLoto [14]
acertosLoto = 0

# Condicionais de verificação:
if apostaLoto01 in lotofacil:
    acertosLoto += 1
elif apostaLoto02 in lotofacil:
    acertosLoto += 1
elif apostaLoto03 in lotofacil:
    acertosLoto += 1
elif apostaLoto04 in lotofacil:
    acertosLoto += 1
elif apostaLoto05 in lotofacil:
    acertosLoto += 1
elif apostaLoto06 in lotofacil:
    acertosLoto += 1
elif apostaLoto07 in lotofacil:
    acertosLoto += 1
elif apostaLoto08 in lotofacil:
    acertosLoto += 1
elif apostaLoto09 in lotofacil:
    acertosLoto += 1
elif apostaLoto10 in lotofacil:
    acertosLoto += 1
elif apostaLoto11 in lotofacil:
    acertosLoto += 1
elif apostaLoto12 in lotofacil:
    acertosLoto += 1
elif apostaLoto13 in lotofacil:
    acertosLoto += 1
elif apostaLoto14 in lotofacil:
    acertosLoto += 1
elif apostaLoto15 in lotofacil:
    acertosLoto += 1
else:
    acertosLoto += 0

print()
print(f'A sua quantidade de acertos na Lotofácil foi: {acertosLoto}')
print()
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)

# Considerações finais: Programa pode ser aprimorado ou programado de varias
# outras formas, porem feito com o intuito de mostrar algumas formas de utilizar 
# as lista, fatiamento e seus métodos em um programa.