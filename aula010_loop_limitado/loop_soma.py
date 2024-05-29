# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 27/05/2024.
# for... range... com somatório.

import os


os.system('cls')

print('-'*50)
print('ESTRUTURA DE CONTROLE SOMATÓRIO')
print('='*50)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'Digite o {var_iteradora + 5}º número: '))
    
    # Cálculo.
    soma += numero # mesma coisa: soma = soma = numero.

print('-'*50)
print(f'A soma dos números é: {soma}')
print('-'*50)
print()