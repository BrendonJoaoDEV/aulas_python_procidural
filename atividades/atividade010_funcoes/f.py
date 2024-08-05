# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 02/08/2024.
# Autor: Brendon João Campos Neves.
# F) Crie uma função que receba 2 listas: 
# - lista 1: nome, peso, idade
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave e valor
# utilizando como base essas duas listas.
# Depois, seu programa deverá imprimir esse dicionário utilizando
# uma estrutura de repetição for.

# Definindo funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def transformas_dicionario(chaves, valores):
    dicionario = {}
    dicionario = dict(zip(chaves, valores))
    return dicionario


# Declarações de variáveis:
lista1 = ['nome', 'peso', 'idade']
lista2 = ['John', 40, 1.8]

limpar_terminal()

# Imprimindo título:
print('.'*79)
print('Transformar listas em dicionários')
print('.'*79)

# Imprimindo informações:
print('-'*79)
print('Lista 1:')
for elemento in lista1:
    print(f'{elemento}', end=', ')
print()
print('Lista 2:')
for elemento in lista2:
    print(f'{elemento}', end=', ')
print()
print('-'*79)

# Processamento de dados:
dicionario = transformas_dicionario(lista1, lista2)

# Saída de dados:
print('='*79)
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')
    print('-'*79)
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)