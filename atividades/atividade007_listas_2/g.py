# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 17/06/2024.
# G) Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.

# Importando as bibliotecas do sistema:
import os


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
for i in range(1, 11):
    numeros.append(int(input(f'Digite o {i}º número: ')))
print('-'*79)

# Processamento de dados:
numeros_ascendente = numeros.sort()
numeros_descendente = numeros.sort(reverse = True)

# Saída de dados:
print('='*79)
print(f)
print('='*79)