# Curso de Desenvolvimento de Sistemas.
# Turma: 18/04/2024.
# Autor: Brendon João Campos Neves.
# Data: 22/04/2024.
# # Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

# Imports
import os


# Limpar o terminal
os.system('cls')

# Entrada
print('-'*70)
dividendo = float(input('Digite o dividendo: '))
divisor = float(input('Digite o divisor: '))
print('-'*70)

# Processamento
quociente = dividendo / divisor

# Saída
print('='*70)
print(f'A divisão entre {dividendo} e {divisor} é: {quociente: .4f}')
print('='*70)
