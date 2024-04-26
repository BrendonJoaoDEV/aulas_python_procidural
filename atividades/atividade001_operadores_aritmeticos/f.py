# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 19/04/2024.
# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

# Imports.
import os


# Limpar o terminal.
os.system('cls')

# Entrada.
print('-'*70)
numero = float(input('Digite um número: '))
print('-'*70)

# Procesaamento.
dobro = numero * 2
triplo = numero * 3

# Saída.
print('='*70)
print(f'O dobro de {numero} é: {dobro}')
print(f'O triplo de {numero} é: {triplo}')
print('='*70)
