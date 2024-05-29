# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 28/05/2024.
# for... range... input... if... else...

import os


os.system('cls')

print('-'*50)
print('ESTRUTURA DE CONTROLE COM INPUT E IF')
print('='*50)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'{var_iteradora + 1}º número: '))
    
    if (numero % 2 ==0):
        print(f'O número {numero} é par')
    else:
        print(f'O númer {numero} é impar')

print('-'*50)
print()