# Curso de Desenvolvimento de sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves
# Data: 05/06/2024.
# c) Faça um programa que receba as informações de base e expoente. Calcule a potência.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo o título.
print('.'*79)
print('CALCULADORA DE POTENCIAÇÃO')
print('.'*79)

# Declarações de variáveis.
base = 0
expoente = 0
potencia = 0

# Entrada de dados.
print('-'*79)
base = input('Digite a base da sua potência: ')
expoente = input('Digite o expoente da sua potência: ')
print('-'*79)

# Processamento de dados.
potencia = base ** expoente

# Saída de dados.
print('='*79)
print(f'O resultado de {base} elevado a {expoente} é {potencia}')
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)