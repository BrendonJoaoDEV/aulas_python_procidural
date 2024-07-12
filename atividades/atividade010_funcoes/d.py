# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 11/07/2024.
# Autor: Brendon João Campoes Neves.
# D) Crie uma função que receba uma temperatura em fahrenheit
# e retorne o valor em graus célsius.

# Definindo funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def fahrenheit_para_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9

    return celcius


# Declarações de variáveis:
temperatura_fahrenheit = 0
temperatura_celcius = 0

limpar_terminal()

print('.'*79)
print('Converter temperatura:')
print('Graus Fahrenheit para Graus Célcius')
print('.'*79)

# Entrada de dados:
print('-'*79)
temperatura_fahrenheit = float(input(
    'Digite a temperatura em Fahrenheit que deseja converter: '))
print('-'*79)

# Processamento de dados:
temperatura_celcius = fahrenheit_para_celcius(temperatura_fahrenheit)

# Saída de dados:
print('='*79)
print(f'{temperatura_fahrenheit: .2f}°F = {temperatura_celcius: .2f}°C')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)