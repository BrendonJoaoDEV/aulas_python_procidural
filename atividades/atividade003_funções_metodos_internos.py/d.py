# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data; 10/05/2024.
# d) Faça um programa que receba um ângulo qualquer.
# Em seguida, calcule o seno, cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.

# Importando as bibliotecas.
import os
import math


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*79)
print('Calculadora trigonométrica')
print('.'*79)

# Entrada.
print('-'*79)
angulo = float(input('Digite o ângulo que deseja saber'
                     ' ceno, cosseno e tangente: '))
print('-'*79)

# Declarações de variáveis.
resposta = ''

# Processamento.
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangete = math.tan(math.radians(angulo))
resposta = (f'Segundo o ângulo {angulo}: seu seno é {seno: .2f}, '
            f'seu cosseno é {cosseno: .2f} e sua tangente é {tangete: .2f}')

# Saída.
print('='*79)
print(resposta)
print('='*79)

# Título de fim.
print('.'*79)
print('Fim do Programa ;)')
print('.'*79)