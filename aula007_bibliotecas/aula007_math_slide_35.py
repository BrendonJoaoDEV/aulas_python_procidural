# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 09/05/2024.
# Biblioteca math: arredondamento para baixo e para cima.

import os
import math


os.system('cls')

print('-'*70)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')
print('='*70)
print()

# Entrada de dados.
numero_decimal = float(input('Entre com um número decimal: '))

# Processamento.
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

# Saída.
print('-'*70)
print(f'O número {numero_decimal} arredondado para cima é:'
      f'{arredondar_para_cima}')
print(f'O número {numero_decimal} arredondado para baixo é:'
      f'`{arredondar_para_baixo}')
print()