# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 19/04/2024.
# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.

# Imports.
import os


# Limpar o terminal.
os.system('cls')

# Entrada
print('-'*70)
numero = int(input('Digite um número inteiro: '))
print('-'*70)

# Processamento.
produto0 = numero * 0
produto1 = numero * 1
produto2 = numero * 2
produto3 = numero * 3
produto4 = numero * 4
produto5 = numero * 5
produto6 = numero * 6
produto7 = numero * 7
produto8 = numero * 8
produto9 = numero * 9
produto10 = numero * 10

# Saída.
print('='*70)
print(f'TABUADA DE MULTIPLICAÇÃO DE {numero}')
print('='*70)
print(f'{numero}×0={produto0}')
print(f'{numero}×1={produto1}')
print(f'{numero}×2={produto2}')
print(f'{numero}×3={produto3}')
print(f'{numero}×4={produto4}')
print(f'{numero}×5={produto5}')
print(f'{numero}×6={produto6}')
print(f'{numero}×7={produto7}')
print(f'{numero}×8={produto8}')
print(f'{numero}×9={produto9}')
print(f'{numero}×10={produto10}')
print('='*70)
