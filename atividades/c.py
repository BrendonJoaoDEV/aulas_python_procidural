# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 18/04/2024.
# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

# Imports
import os


# Limpar o terminal
os.system('cls')

# Entrada
print('-'*70)
print('DIGITE AS NOTAS DO ALUNO')
print('-'*70)
nota1 = float(input('Entre com a 1ª nota: '))
nota2 = float(input('Entre com a 2ª nota: '))
nota3 = float(input('Entre com a 3ª nota: '))
nota4 = float(input('Entre com a 4ª nota: '))
print('-'*70)

# Processamento
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

# Saída
print('='*70)
print(f'A média de notas do aluno é: {media}')
print('='*70)
