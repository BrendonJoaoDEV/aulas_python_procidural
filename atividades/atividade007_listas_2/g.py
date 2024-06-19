# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 17/06/2024.
# G) Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.

# Importando as bibliotecas do sistema:
import os
import random


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
numeros = []
numeros_ascendente = []
numeros_descendente = []

# Exibindo título:
print('.'*79)
print('NÚMEROS EM ORDEM ASCENDENTE E DESCENDENTE')
print('.'*79)

# Entrada de dados:
print('-'*79)
for i in range(0, 10):
    numeros.append(random.randint(0, 100))
print(f'Lista de números aleatórios gerada: {numeros}')
print('-'*79)

# Processamento de dados:
numeros_ascendente = numeros.copy()
numeros_ascendente.sort()
numeros_descendente = numeros.copy()
numeros_descendente.sort(reverse = True)

# Saída de dados:
print('='*79)
print(f'Números em ordem aleatória: {numeros}')
print(f'Números em ordem ascendente: {numeros_ascendente}')
print(f'Números em ordem descendente: {numeros_descendente}')
print('='*79)

# Exibindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)