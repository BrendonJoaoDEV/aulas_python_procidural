# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 12/06/2024.
# List comprehension para aplicar 10% a todos os elementos de uma lista e gerar outra lista.

import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: List Comprehensions [ ]')
print('='*70)

lista_numeros = [100, 200, 300, 400, 500, 600]

# Calcular e adicionar 10%.
lista_com_juros = []

for item in lista_numeros:
    
    lista_com_juros.append(item + (item * .10))

print('Aplicar 10% de juros: forma normal')
print(f'Lista com juros de 10%: {lista_com_juros}')
print()

# List Comprehensions.
lista_com_juros_2 = [item + (item * 10) for item in lista_numeros]
print('Aplicar 10% de juros: List COmprehensions')
print(f'Lista triplicada: {lista_com_juros_2}')