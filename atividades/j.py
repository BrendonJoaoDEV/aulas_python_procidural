# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 22/04/2024.
# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

# Imports.
import os


# Limpando o terminal.
os.system('cls')

# Entrada.
print('-'*70)
base = float(input('Digite o valor da base do retângulo: '))
altura = float(input('Digite o valor da altura do retângulo: '))
print('-'*70)

# Processamento.
# Fórmula do perímetro é Perímetro = 2×(base+altura).
perimetro = 2 * (base + altura)

# Saída.
print('='*70)
print(f'O perímetro do retângulo é {perimetro}')
print('='*70)
