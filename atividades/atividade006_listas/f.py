# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 16/06/2024.
# F) Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
entrada = ''
nomes = []
indice = 0
nome = ''

# Entrada de dados:
print('-'*79)
while True:
    entrada = input('Digite 5 nomes separados por espaços: ')
    nomes = entrada.split()
    if (len(nomes) > 5):
        print('Digite apenas cinco nomes!')
        continue
    else:
        break
print('-'*79)

# Processamento e saída de dados:
print('='*79)
print('Nomes e seus respectivos índices')
for indice, nome in enumerate(nomes):
    print(f'Índice: {indice} Nome: {nome}')
print('='*79)

# Imprimindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)