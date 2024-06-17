# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 16/06/2024.
# E) Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('clear')

# Declarações de variáveis:
nome_chute = ''
nome_sistema = 'Pedro'

# Imprimindo título:
print('.'*79)
print('JOGO: ADIVINHE O NOME DO SISTEMA')
print('.'*79)

# Entrada de dados:
print('-'*79)
while True:
    nome_chute = input('Chute qual é o nome do sistema: ').capitalize()
    if nome_chute == nome_sistema:
        