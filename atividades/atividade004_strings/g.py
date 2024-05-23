# Cursos de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 22/05/2024.
# G) Faça um programa que receba um número inteiro e mostre na tela:
# A quantidade de unidades, 
# a quantidade de dezenas, 
# a quantidade de centenas e 
# a quantidade de milhares.

# Importando as bibliotecas.
import os


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*79)
print('DIVISÃO DO NÚMERO INTEIRO POR SUAS CASAS')
print('.'*79)

# Entrada de dados.
print('-'*79)
numero = int(input('Digite um número inteiro: '))
print('-'*79)

# Declaração de variáveis.
unidades = 0
dezenas = 0
centenas = 0
milhares = 0

# Processamento de dados.
unidades = (numero//1) % 10
dezenas = (numero//10) % 10
centenas = (numero//100) % 10
milhares = (numero//1000) % 10

# Saída de dados.
print('='*79)
print(f'Esse número tem: {unidades} unidades.')
print(f'Esse número tem: {dezenas} dezenas.')
print(f'Esse número tem: {centenas} centenas.')
print(f'Esse número tem: {milhares} unidades de milhar.')
print('='*79)

# Título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)