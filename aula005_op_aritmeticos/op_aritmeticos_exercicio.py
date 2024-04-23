# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 23/04/2024
# Seguindo os passos anteriores, desenvolva o restante:
# Acrescente a raiz quadrada e a raiz cúbica.

# Imports.
import os

# Limpando o terminal.
os.system('cls')

# Entrada.
print()
print('--- RADICIAÇÃO')
print('-'*70)
radicando = float(input('Entre com o radicando: '))
indice = float(input('Entre com o radical: '))

# Processamento.
raiz = radicando ** (1/indice)

# Saída.
print('='*70)
print('RESULTADO')
print('-'*70)
print(f'A raiz de {radicando} é: {raiz}')
