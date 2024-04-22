# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data:19/04/2024.
# Faça um programa que converta metros em centímetros e milímetros.

# Imports
import os


# Limpar o terminal
os.system('cls')

# Entrada
print('-'*70)
metros = float(input('Digite um valor em metros: '))
print('-'*70)

# Processamento
centimetros = metros * 100
milimetros = metros * 1000

# Saída
print('='*70)
print(f'{metros} metros são {centimetros} centímetros.')
print(f'{metros} metros são {milimetros} milímetros.')
print('='*70)
