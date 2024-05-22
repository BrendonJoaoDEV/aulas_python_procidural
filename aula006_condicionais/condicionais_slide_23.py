# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 24/04/2024.
# Estudo de Condicionais: parte 1.
# Objetivo: Verificando um valor decimal.

import os


os.system('cls')

print('-'*70)
print('Estudo de Condicional: Parte 1')
print('='*70)

# Entrada.
numero = float(input('Digite um número: '))
resposta = ''

# Condicional.
if numero % 2 == 0:
    resposta = f'O número {numero} é par!'
else:
    resposta = f'O número {numero} é ímpar!'

# Saída.
print('='*70)
print(resposta)

print('Fim do programa!\n') # \n salta uma linha.