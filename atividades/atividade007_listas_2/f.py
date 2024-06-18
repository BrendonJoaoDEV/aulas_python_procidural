# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 17/06/2024.
# F) Faça um programa que recebe 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
numeros = []
pares = []
impares = []

# Exibindo o título:
print('.'*79)
print('SEPARANDO NÚMEROS EM PARES E ÍMPARES')
print('.'*79)

# Entrada de dados:
print('-'*79)
for i in range(1, 8):
    numeros.append(int(input(f'Digite o {i}º número: ')))
print('-'*79)

# Processamento de dados:
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Saída de dados:
print('='*79)
print(f'Sua lista de números é: {numeros}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
print('='*79)

# Exibindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)