# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 10/06/2024.
# Estrutura de dados: Listas [] + for... + enumerate() para enumerar o indice dos itens de uma lista.

import os


os.system('cls')

print('-' * 70)
print('SAÍDA COM FOR... ENUMERATE()')
print('=' * 70)

soma = 0

# Criando uma lista.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorrendo a lista com o enumerate().
# O comando enumerate adiciona um indice.
# para cada valor de nossa lista.
# Start opcional, para não começar no índice 0.
# Enumerate(listaNumeros, start - 1)

# Para cada número dentro da lista de números, enumere com um índice.
for indice, numero in enumerate(lista_numeros):
    soma += numero # Soma os números.
    print(f'Indice: {indice} = Número: {numero}')

print('-'*70)
print(f'A soma de todos os números é: {soma}')
print('Fim do programa!')
print('-'*70)