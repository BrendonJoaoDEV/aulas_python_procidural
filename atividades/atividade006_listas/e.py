# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 16/06/2024.
# E) Faça um programa que leia as vogais, depois mostre-as em ordem inversa.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
vogais = ['a', 'e', 'i', 'o', 'u']
vogais_contrario = []

# Imprimindo título:
print('.'*79)
print(f'Invetendo a ordem das vogais: {vogais}')
print('.'*79)

# Processamento:
vogais.sort()
vogais_contrario = vogais.copy()
vogais_contrario.sort(reverse = True)

# Saída de dados:
print('='*79)
print(f'Vogais: {vogais}')
print(f'Vogais em ordem inversa: {vogais_contrario}')
print('='*79)

# Imprimindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)