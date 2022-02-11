# função:
def painel_academia():
    """ [Função que printa ARTCII= painel academia]
     """    
    print("""
     ____________________________________________   
    | Digite um numero para definir uma função   |
    | para o programa Academia:                  |
    |                                            |
    | 1 = CADASTRAR                              |               
    |                                            |
    | 2 = LISTAR ALUNOS CADASTRADOS              |
    |                                            |
    |               0 = SAIR                     |
    |____________________________________________|
    """)

def print_error_valor():
    """[Função que printa o erro de entrada de valores]"""
    
    print("""
Códico = Numeros inteiros.
Nome = Apenas texto.
Altura = Apenas numeros inteiros ou flutuantes.
Peso = Apenas numeros inteiros ou flutuantes.
                                            """)

def formador_Dict(lista_1, lista_2):
    """[Função que converte listas em dicionario]

    Args:
        lista1 ([List]): [Lista que vai ser a chave]
        lista2 ([List]): [Lista que vai ser o valor]

    Returns:
      newList  [Dict]: [Novo dicionario com chave e valores das listas inseridas]
    """
    newList = dict(zip(lista_1, lista_2))
    return newList

def media_altura_peso(lista_alunos):
    """[Função que calcula a media e altura dos aluno]

    Args:
        lista_alunos ([Dict): [lista com dicionarios de alunos]

    Returns:
      media_alt  [float]: [resultado da media da altura]
      media_peso [float]: [resultado da media do peso]
    """
    somar_alt = 0
    somar_peso = 0
    for registro in lista_alunos:
        for chave, valores in registro.items():
            if chave == 'altura':
                somar_alt += valores
            elif chave == 'peso':
                somar_peso += valores
    media_alt = somar_alt / len(lista_alunos)
    media_peso = somar_peso / len(lista_alunos)
    return media_alt, media_peso

