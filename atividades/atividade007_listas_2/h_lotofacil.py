# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 18/06/2024.
# H) Faça um programa que sorteia os números da Mega Sena e da Lotofácil.

# Importando as bibliotecas do sistema:
import os
import random


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
numeros = []
sorteados = []

# Exibindo título:
print('.'*79)
print('SORTEANDO OS NÚMEROS DA LOTOFÁCIL')
print('.'*79)

# Processamento:
for numero in range(1, 26):
    numeros.append(numero)

sorteados = random.sample(numeros, 15)
sorteados.sort()

# Saída de dados:
print('='*79)
print(f'Os 15 números sorteados da Lotofácil são: {sorteados}')
print('='*79)

# Exibindo título de fim:
print('.'*79)
print('Fim do sorteio! Obrigado!')
print('.'*79)