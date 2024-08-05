# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 11/07/2024.
# Autor: Brendon João Campos Neves.
# E) Crie uma função que receba a altura e o peso de uma pessoa.
# Depois retorne o seu IMC.

# Definindo funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

# Declarações de variáveis:
peso = 0.0
altura = 0.0

limpar_terminal()

print('.'*79)
print('Calcular IMC:')
print('.'*79)

# Entrada de dados:
print('-'*79)
peso = float(input('Digite seu peso: '))
altura =float(input('Digite sua altura: '))
print('-'*79)

# Processamento de dados:
imc = calcular_imc(peso, altura)

# Saída de dados:
print('='*79)
print(f'Seu IMC é {imc: .2f}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)