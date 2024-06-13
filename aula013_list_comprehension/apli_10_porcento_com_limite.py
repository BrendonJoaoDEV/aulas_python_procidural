# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 12/06/2024.
# List comprehension para aplicar 10% a todos os elementos de uma lista e gerar outra lista.

import os


os.system('cls')

print('-'*70)
print(f'ESTRUTURA DE DADOS: List Comprehensions [ ]')
print('='*70)

lista_precos = [100, 200, 300, 400, 500, 600]

# Aplicando 10%.
lista_com_juros = []

for valor in lista_precos:
    if valor < 300:
        lista_com_juros.append(valor + (valor * .10))

print('Aplicar juros em condicional: forma normal')
print(f'Lista com juros: {lista_com_juros}')
print()

# List Comprehensions.
lista_com_juros_2 = [valor + (valor * .10)
                     for valor in lista_precos if valor < 300]

print('Aplicar juros em condicional: List Comprehensions')
print(f'Lista com juros: {lista_com_juros_2}\n')