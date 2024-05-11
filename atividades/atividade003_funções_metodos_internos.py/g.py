# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 10/05/2024.
# g) Faça um programa que peça os valores de a, b e c de uma equação do 2º grau.
# Calcule as raízes da equação do 2º grau seguindo a fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

# Importando as bibliotecas.
import os
import math


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*79)
print('Calculadora de equações de segundo grau')
print('.'*79)

# Entrada.
print('-'*79)
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
print('-'*79)

# Declarações de variáveis
discriminante = ''
segundo_grau_mais = ''
segundo_grau_menos = ''
resposta = ''
resposta_2 = ''
resposta_3 = ''

# Processamento.
discriminante = b**2 -4 * a * c
if discriminante > 0:
    segundo_grau_mais = (-b + (math.sqrt(discriminante))) / (2 * a)
    segundo_grau_menos = (-b - (math.sqrt(discriminante))) / (2 * a)
    resposta = f'Levando em consideração a={a}, b={b} e c={c}.'
    resposta_2 = f'A raiz caso + discriminante: x={segundo_grau_mais}.'
    resposta_3 = f'A raiz caso - discriminante: x={segundo_grau_menos}.'
else:
    resposta = f'Não é possível calcular as raízes dessa equação!'
    resposta_2 = f'Porque a={a}, b={b} e c={c} geram um discriminante'
    resposta_3 = f'negativo ou igual a zero.'

# Saída.
print('='*79)
print(resposta)
print(resposta_2)
print(resposta_3)
print('='*79)

# Título de fim.
print('.'*79)
print('Fim do programa ;)')
print('.'*79)