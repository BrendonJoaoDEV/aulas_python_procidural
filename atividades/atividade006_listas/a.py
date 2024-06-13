# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 12/06/2024.
# # A) Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Declaração da lista.
lista = [1, 2, 3, 5, 6]

# Imprimindo dados iniciais.
print('-'*79)
print(lista)
print('-'*79)

# Processamento de dados
lista_processada = lista.insert(2, 4)

# Imprimindo dados processados.
print('='*79)
print(lista_processada)
print('='*79)