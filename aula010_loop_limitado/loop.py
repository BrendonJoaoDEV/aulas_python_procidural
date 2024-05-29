# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 27/05/2024.
# for i in range(start, stop, step)

import os


os.system('cls')

print('-'*79)
print('ESTRUTURA DE CONTROLE FOR RANGE')
print('='*79)

print()

for var_iteradora in range(1, 7):
    # end = coloca os números em uma mesma lista.
    print(f'Valor: {var_iteradora}', end =' | ')

print()
print()

# OU.

inicio = 1
fim = 7
passo = 2

for var_iteradora in range(inicio, fim, passo):
    # end = coloca os números em uma mesma linha.
    print(f'Valor: {var_iteradora}', end = ' | ')

print()
print()