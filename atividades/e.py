# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 19/04/2024.
# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

# Imports.
import os


# Limpar o terminal.
os.system('cls')

# Entrada.
print('-'*70)
numero = int(input('Digite um número inteiro: '))
print('-'*70)

# Processamento.
antecessor = numero - 1
sucessor = numero + 1

# Saída.
print('='*70)
print(f'O antecessor de {numero} é: {antecessor}')
print(f'O sucessor de {numero} é: {sucessor}')
print('='*70)
