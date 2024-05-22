# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 12/04/2024.
# Estudo de Condicionais: parte 2
# Objetivo: Prática com condicionais semples e aninhadas.

import os


os.system('cls')

# Declarações.
a = 10
b = 5
resposta = ''

print('-'*70)
print('Estudo de Condicional (Simples)')
print('='*70)

# Condicional Simples.
if a > b:
    resposta = f'{a} é maior que {b}'
else:
    resposta = f'{a} não é maior que {b}'

# Saída.
print('-'*70)
print(resposta)

# Declarações.
a = 5
b = 5

print('-'*70)
print('Estudo de Condicional (Aninhada)')
print('='*70)

# Condicional Aninhada.
if a > b:
    resposta = f'{a} é maior que {b}'
elif a < b:
    resposta = f'{a} é menor que {b}'
else:
    resposta = f'Os valores são iguais: {a} = {b}'
    
print('-'*70)
print(resposta)
print('-'*70)
print()