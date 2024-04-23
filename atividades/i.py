# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 22/04/2024.
# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.

# Imports.
import os


# Limpando o terminal.
os.system('cls')

# Entrada.
print('-'*70)
reais = float(input('Digite um valor em reais: '))
print('-'*70)

# Processamento.
dolares = reais / 5.17

# Saída.
print('='*70)
print(f'{reais} reais correspondem a {dolares} dolares')
print('='*70)
