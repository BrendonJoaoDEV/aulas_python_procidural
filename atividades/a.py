# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data:18/04/2024.
# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores.

# Imports.
import os


# Limpar o terminal
os.system('cls')

# Entrada
print('-'*70)
print('ENTRE COM OS NÚMEROS')
print('-'*70)
valor1 = float(input('Entre com o 1ª valor: '))
valor2 = float(input('Entre com o 2ª valor: '))
valor3 = float(input('Entre com o 3ª valor: '))

# Processamento
soma = valor1 + valor2 + valor3
produto = valor1 * valor2 * valor3

# Saída
print('='*70)
print('RESULTADOS')
print('='*70)
print(f'A soma de {valor1} + {valor2} + {valor3} é: {soma}')
print(f'A multiplicação de {valor1} × {valor2} × {valor3} é: {produto}')
print('='*70)