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

# Entrada dados.
print('-'*70)
radicando = float(input('Digite o número que deseja saber a raiz quadrada: '))
print('-'*70)
resposta = ''
raiz_arredondada_cima = ''
raiz_arredondada_baixo = ''

# Processamento de dados.
raiz_quadrada = math.sqrt(radicando)

# Validação da resposta.
if radicando < 0:
    resposta = (f'O radicando é negativo, portanto o resultado será '
    f'um número complexo')
elif raiz_quadrada == float(radicando):
    raiz_arredondada_cima = math.ceil(raiz_quadrada)
    raiz_arredondada_baixo = math.floor(raiz_quadrada)
    resposta = (f'O radicando {radicando} gerá a raiz não exata '
    f'{raiz_quadrada}, por isso pode ser arrendodado para'
    f'{raiz_arredondada_cima} ou {raiz_arredondada_baixo}')
else:
    resposta = f'A raiz do número {radicando} é {raiz_quadrada}'

# Saída de dados.
print('='*79)
print(resposta)
print('='*79)

# Título fim.
print('.'*79)
print('Fim do pograma! Obrigado!')
print('.'*79)