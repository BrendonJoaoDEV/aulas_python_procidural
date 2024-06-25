# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 24/06/2024.
# Exemplo de tupla:

import os


os.system('cls')

nomes = ['Ágata', 'Bia', 'Coly', 'Isis']

for indice, nome in enumerate(nomes):
    # Cria uma tupla contendo o índice e o nome da pessoa atual.
    minha_tupla = (indice, nome)
    # A variável minha_tupla é utilizada para acessar o
    # índice e o nome armazenados na tupla.
    # Mas posso acessar diretamente os elementos 'indice' e 'nome'.
    print(f'O nome "{minha_tupla[1]}", posição {minha_tupla[0]} da lista.')
    print(f'O nome "{nome}", posição {indice} da lista.')
    print('-'*70)
