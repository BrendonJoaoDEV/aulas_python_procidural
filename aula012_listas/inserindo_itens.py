# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 10/06/2024.
# Estrutura de dados: Listas [] + insert().

import os


os.system('cls')

# Lista original.
lista = [1, 2, 3 ,4]

# Pedindo ao usuário para fornecer a
# posição e o elemento a ser inserido.
posicao = int(input('Posição onde deseja inserir o elemento: '))
elemento = input('Elemento a ser inserido: ')

# Verifica se a posição fornecida pelo usuário é válida.
if posicao >= 0 and posicao <= len(lista):
    # Inserindo o elemento na lista na posição especificada pelo usuário.
    lista.insert(posicao, elemento)
    print('List após a inserção:', lista)
else:
    print(f'Posição fora do intervalo de 0, {len(lista)}')