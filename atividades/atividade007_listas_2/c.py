# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 16/06/2024.
# C) Faça um programa que preencha uma lista com 50 números aleatórios.
# Depois fatie essa lista em 5 listas de 10 elementos.

# Impotando as bilbiotecas do sistema:
import os
import random

# Limpando o terrminal:
os.system('clear')

# Declarações de variáveis:
numeros = []
numero = 0
sublistas = []

# Imprimindo o título:
print('.'*79)
print('GERANDO INTERVALO DE NÚMEROS ALEATÓRIOS E DIVIDINDO O EM GRUPOS DE 10')
print('.'*79)

# Processamento de dados:
# Gerando 50 números aleatórios:
for numero in range(0, 50):
    numero = random.randint(0, 1000)
    numeros.append(numero)

# Dividindo esses números em grupos de 10:

# Saída de dados:
print('='*79)
print(f'Lista completa: {numeros}')
print(f'Lista dividida a cada 10 números: ')
print('='*79)

# Imprimindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)