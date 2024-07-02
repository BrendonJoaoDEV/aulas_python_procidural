# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/07/2024.
# J) Faça um programa para criar um dicionário com nomes de frutas.
# Em seguida verifique se tem abacaxi nos valores.

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('clear')

# Declarações de variáveis:
dicionario = {}
chave = ''
valor = ''

# Impressão do título:
print('.'*79)
print('Jogo de adivinhação:')
print('Tema: Frutas')
print('.'*79)

# Entrada de dados:
while True:
    print('(sistema) - Adivinhe a fruta que estou pensando...')
    while True:
        