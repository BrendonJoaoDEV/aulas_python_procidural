# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/07/2024.
# I) Faça um programa para criar um dicionário com 4 elementos.
# Depois imprima a lista completa, delete o último elemento e mostre uma listagem nova.

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('cls')

# Declarações de variáveis:
dicionario = {}
chave = ''
valor = ''

# Impressão do título:
print('.'*79)
print('Processamento de dicionário:')
print('.'*79)

# Entrada de dados:
print('-'*79)
for i in range(1, 5):
    chave = str(input(f'Digite a chave do {i}º elemento: '))
    valor = str(input(f'Digite o valor do {i}º elemento: '))
    print('-'*79)
    dicionario[chave] = valor

# Saída antes:
print('='*79)
print('Dicionário antes:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')
    print('-'*79)
print('='*79)

# Processamento de dados:
dicionario.popitem()

# Saída depois:
print('='*79)
print('Dicionário depois:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')
    print('-'*79)
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)