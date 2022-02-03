# Curso técnico de informática
# Autor: Denilsom Lobo de Souza
# Data de início: 06/12/2021
# Data de término: 06/12/2021
# Atividade 009. Denilsom. Turma 11. Letra B.

# Programa de lista de compras

# Importando as bibliotecas:
import os


# Limpando o terminal:
os.system('cls')

# Declarações
loja1 = {'arroz','feijão','macarrão','carne',}
loja2 = {'arroz','feijão','macarrão','sorvete'}
novaLoja = set()

# Texto de entrada:
print('='*80)
print('''
  ______         _                                    
 |  ____|       | |                                   
 | |__     ___  | |_    ___     __ _   _   _    ___   
 |  __|   / __| | __|  / _ \   / _` | | | | |  / _ \  
 | |____  \__ \ | |_  | (_) | | (_| | | |_| | |  __/  
 |______| |___/  \__|  \___/   \__, |  \__,_|  \___|  
                                  | |                 
                                  |_|                 
''')
print('='*80)

# Estrutura de repetição para verificar estoque das outras lojas:
while(True):
    # Validação de verificação:
    verListas = str(input('Deseja ver o que tem no estoque '+
    'das suas lojas? (s/n): ')).lower().strip()
    print()
    if(verListas != 's') and (verListas != 'n'):
        print('Entrada invalida ...')
        print()
    # Condicionais de verificação:
    else:
        if(verListas == 'n'):
            os.system('cls')
            break
        elif(verListas == 's'):
            print()
            print('No estoque das suas lojas possui:')
            print(f'Na loja 1 = {loja1}')
            print(f'Na Loja 2 = {loja2}')
            print()

# Estrutura de repetição de entrada de dados na lista do estoque novo:
while(True):
    print('='*80)
    print('''
  ______         _                                    
 |  ____|       | |                                   
 | |__     ___  | |_    ___     __ _   _   _    ___   
 |  __|   / __| | __|  / _ \   / _` | | | | |  / _ \  
 | |____  \__ \ | |_  | (_) | | (_| | | |_| | |  __/  
 |______| |___/  \__|  \___/   \__, |  \__,_|  \___|  
                                  | |                 
                                  |_|                 
''')
    print('='*80)
    # Entrada de dados:
    add = str(input('Insira o que tem no estoque da nova loja. '+
    ' ("p" = pular): ').lower().strip())
    print()
    # Condicional para pular:
    if (str(add) == 'p'):
        os.system('cls')
        break
    # Condicional para validação de acressimo no set:
    elif (True):
        # Adicionar no set.
        novaLoja.add(add)

    # Estrutura de repetição para validação e verificação da montagem do set:
    while (True):
        print()
        # Entrada para validação e verificação da montagem do set:
        sair = str(input('Se deseja continuar adicionando a lista use ("s")'+
        ' caso queira ver sua lista ate agora use ("n") para sair use ("p")'+
        'na hora de inserir: '))
        print()
        # Condicionais para validação e verificação da montagem do set:
        if (sair != 's') and (sair != 'n'):
            print('Entrada invalida...')
            print() 
        elif (sair == 's'):
            os.system('cls')
            break
        elif (sair == 'n'):
            print('-'*80)
            print(f'No estoque da nova loja possui: {novaLoja}')
            print('-'*80)

            
# Estrutura de repetição para verificar de deseja remover algo da lista.
print('='*80)
print('''
  ______         _                                    
 |  ____|       | |                                   
 | |__     ___  | |_    ___     __ _   _   _    ___   
 |  __|   / __| | __|  / _ \   / _` | | | | |  / _ \  
 | |____  \__ \ | |_  | (_) | | (_| | | |_| | |  __/  
 |______| |___/  \__|  \___/   \__, |  \__,_|  \___|  
                                  | |                 
                                  |_|                 
''')
print('='*80)
while (True):
    # Entrada para remover algo dso set da nova loja:
    comando = str(input('Deseja remover algum item da lista '+
    ' que possui no seu estoque da loja nova ? (s/n): '))
    print()
    # Validação:
    if (comando != 's') and (comando != 'n'):
        print('Entrada invalida ...')
        print()
    # Comando para remover no set:
    elif (comando == 's'):
        remover = str(input('Digite o que você quer remover da lista: '))
        print()
        novaLoja.discard(remover)
        print('Item removido ...')
        print()
    # Saida do laço:
    elif(comando == 'n'):
        os.system('cls')
        break

# Estrutura de repetição para verificar se a nova loja possui 
# itens das outras lojas.
print('='*80)
print('''
  ______         _                                    
 |  ____|       | |                                   
 | |__     ___  | |_    ___     __ _   _   _    ___   
 |  __|   / __| | __|  / _ \   / _` | | | | |  / _ \  
 | |____  \__ \ | |_  | (_) | | (_| | | |_| | |  __/  
 |______| |___/  \__|  \___/   \__, |  \__,_|  \___|  
                                  | |                 
                                  |_|                 
''')
print('='*80)
while (True):
    # Entrada para remover algo dso set da nova loja:
    comando = str(input('Deseja saber se o estoque da Nova loja '+
    ' esta igual nas outras ? (s/n): '))
    print()
    # Validação:
    if (comando != 's') and (comando != 'n'):
        print('Entrada invalida ...')
        print()
    # Comando para verificar se um set esta igual a outro set:
    elif (comando == 's'):
        verificar1 = novaLoja.issuperset(loja1)
        verificar2 = novaLoja.issuperset(loja2)
        # Condicionais de verificação verdadeiro ou falso:
        if (verificar1 == True):
           print()
           print('A nova loja está igual a Loja 1')
           print()
        else:
            print()
            print('A nova loja não está igual a Loja 1')
            print()
        if (verificar2 == True):
           print()
           print('A nova loja está igual a Loja 2')
           print()
        else:
            print()
            print('A nova loja não está igual a Loja 2')
            print()

    # Saida do laço:
    elif(comando == 'n'):
        os.system('cls')
        break

# Estrutura de repetição para verificar relatorio no estoque.
print('='*80)
print('''
  ______         _                                    
 |  ____|       | |                                   
 | |__     ___  | |_    ___     __ _   _   _    ___   
 |  __|   / __| | __|  / _ \   / _` | | | | |  / _ \  
 | |____  \__ \ | |_  | (_) | | (_| | | |_| | |  __/  
 |______| |___/  \__|  \___/   \__, |  \__,_|  \___|  
                                  | |                 
                                  |_|                 
''')
print('='*80)
while (True):
    # Entrada para verificação de relatorio no estoque:
    print()
    comando = str(input('Deseja saber o relatorio '+
    'do que possui no seu estoque ? (s/n): '))
    print()
    # Validação:
    if (comando != 's') and (comando != 'n'):
        print('Entrada invalida ...')
        print()
    # Comando ja juntar os sets com itens de estoque:
    elif (comando == 's'):
        # Operações:
        todosItens = loja1.union(loja2,novaLoja)
        diferencaL1 = novaLoja.difference(loja1)
        diferencaL2 = novaLoja.difference(loja2)
        diferencaL3 = novaLoja.difference(loja1,loja2)
        ambas1 = novaLoja.intersection(loja1)
        ambas2 = novaLoja.intersection(loja2)
        ambas3 = novaLoja.intersection(loja1,loja2)

        # Saidas:
        print('='*80)
        print('Estoque das lojas: ')
        print()
        print(f'Loja 1 = {loja1}')
        print()
        print(f'Loja 2 = {loja2}')
        print()
        print(f'Nova loja = {novaLoja}')
        print()
        print('='*80)
        print()
        print(f'Os itens que possui na nova loja que não possui na '+
        f'loja 1 são: {diferencaL1}')
        print('-'*80)
        print()
        print(f'Os itens que possui na nova loja que não possui na '+
        f'loja 2 são: {diferencaL2}')
        print('-'*80)
        print()
        print(f'Os itens que não possui nem na loja 1 nem na loja 2 '+
        f'apenas na nova loja são: {diferencaL3}')
        print('-'*80)
        print()
        print('='*80)
        print()
        print(f'Os itens que possui na loja 1 e possui na '+
        f'nova loja são: {ambas1}')
        print()
        print(f'Os itens que possui na loja 2 e possui na '+
        f'nova loja são: {ambas2}')
        print()
        print(f'Os itens que possui na loja 1 e na loja 2 e também na '+
        f'nova loja são: {ambas3}')
        print()
        print('='*80)
        print()
        print('Na suas lojas possui esses itens no estoque:')
        # Estrutura de repetição para listar os itens no estoque:
        for i, itemV in enumerate(todosItens):
            print(f'Indicie: {i} | Item : {itemV}')
    # Saida do laço:
    elif(comando == 'n'):
        os.system('cls')
        break
# Texto de encerramento:  
print('='*80)
print('''
  ______         _                                    
 |  ____|       | |                                   
 | |__     ___  | |_    ___     __ _   _   _    ___   
 |  __|   / __| | __|  / _ \   / _` | | | | |  / _ \  
 | |____  \__ \ | |_  | (_) | | (_| | | |_| | |  __/  
 |______| |___/  \__|  \___/   \__, |  \__,_|  \___|  
                                  | |                 
                                  |_|                 
''')
print('='*80)
print()
print('FIM DO PROGRAMA')
print()
print('='*80)


# Considerações finais: Programa pode ser aprimorado ou programado de varias
# outras formas, porem feito com o intuito de mostrar algumas formas de utilizar 
# os Sets e seus métodos em um programa.