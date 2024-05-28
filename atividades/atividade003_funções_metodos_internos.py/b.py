# Curso de Desenvolvimento de sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves
# Data: 27/05/2024.
# b) Faça um programa que receba 2 valores, faça a divisão entre eles.
# Se a divisão não for inteira, o programa deverá arredondar o resultado para cima e para baixo. 
# Faça a validação para divisão por 0.

# Importando as bibliotecas.
import os
import math


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('SISTEMA DE DIVISÃO')
print('.'*79)

# Entrada de dados.
print('-'*79)
dividendo = input('Digite o dividendo: ')
divisor = input('Digite o divisor: ')
print('-'*79)

# Declarações de variáveis.
quociente = 0
resposta = ''
arredondado_cima = ''
arredondado_baixo = ''

# Validação de dados
if divisor == 0:
    resposta = 'Não é possivel realizar nenhuma divisão por zero.'
elif divisor == str(divisor):
    resposta = 'Seu divisor não é um número'
elif dividendo == str(dividendo)
    resposta = 'Seu divisor não é um número'
else:
    resposta = ''

# Processamento de dados.
quociente = dividendo / divisor
if type(quociente) == float:
    arredondado_cima = math.ceil(quociente)
    arredondado_baixo = math.floor(quociente)
    resposta = (f'Seu resultado é {quociente}, por ser não inteiro,'
                f'então pode ser arredondado para {arredondado_cima}'
                f'ou {arredondado_baixo}.')
else:
    resposta = f'O resultado de sua divisão {quociente}'

# Saída de dados.
print('='*79)
print(resposta)
print('='*79)

# Título de fim.
print('.'*79)
print('FIm do programa! Obrigado!')
print('.'*79)