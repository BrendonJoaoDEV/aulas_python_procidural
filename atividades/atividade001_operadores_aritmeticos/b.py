# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 18/04/2024.
# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

# Imports.
import os
import datetime


# Limpar o terminal.
os.system('cls')

# Entrada.
print('-'*70)
nascimento = str(input('Digite o ano de seu nascimento: '))
print('-'*70)

# Processamento.
ano_atual = datetime.datetime.now ().year
idade = int(ano_atual) - int(nascimento)

# Saída.
print('='*70)
print(f'Sua idade é: {idade} anos!')
print('='*70)
