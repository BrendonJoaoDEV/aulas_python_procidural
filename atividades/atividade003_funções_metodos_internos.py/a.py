# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon Jõao Campos Neves.
# Data: 09/05/2024.
# a) Faça um programa que receba um valor e mostre sua raiz quadrada.
# Para raízes que não são exatas, arredonde para cima ou para baixo.
# Faça a validação para números negativos, avisando ao usuário que o resultado será um número complexo.

# Importando as bibliotecas.
import os
import math


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*70)
print('Sistema para calcular raiz quadrada')
print('.'*70)

# Entrada/Declaração de variáveis.
print('-'*70)
radicando = float(input('Digite o número que deseja saber a raiz quadrada: '))
print('-'*70)
resposta = ''
raiz_arredondada = ''

# Processamento.
raiz_quadrada = math.sqrt(radicando)

if radicando < 0:
    resposta = (f'O radicando é negativo, portanto o resultado será '
    f'um número complexo')
elif raiz_quadrada == float(radicando):
    raiz_arredondada = math.ceil(raiz_quadrada)
    resposta = (f'O radicando {radicando} gerá a raiz não exata '
    f'{raiz_quadrada}, por isso pode ser '