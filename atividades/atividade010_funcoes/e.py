# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 11/07/2024.
# Autor: Brendon João Campoes Neves.
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


limpar_terminal()

print('.'*79)
print('Calcular IMC:')
print('.'*79)
# Entrada de dados:
print('-'*79)
peso = float('Digite seu peso: ')
altura = float('Digite sua altura: ')
print('-'*79)