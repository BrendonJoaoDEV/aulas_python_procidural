# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 30/06/2024.
# D) Faça um programa para criar um dicionário com 5 cores.
# Depois, imprima as chaves e os valores deste dicionário.

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('cls')

# Declarações de variáveis:
cores = {
    'Yellow' : 'Amarelo',
    'Red' : 'Vermelho',
    'Blue' : 'Azul',
    'Green' : 'Verde',
    'Orange' : 'Laranja'}

cor = {}

opcao = ''
chave = ''
valor = ''

# Impressão do título:
print('.'*79)
print('Dicionário de Cores:')
print('.'*79)

# Escolha do usuário:
print('-'*79)
opcao = str(input('Deseja usar o dicionário pré-definido? (s/n) ')).lower()
print('-'*79)

if opcao == 's':
    # Imprimindo dicionário padrão:
    print('='*79)
    for chave, valor in cores.items():
        print(f'{chave} : {valor}')
    print('='*79)
else:
    cores.clear() # Limpa dicionário padrão.
    cores = list(cores) # Transforma ele em uma lista.
    print('-'*79)
    
    # Entrada de dados:
    for i in range(1, 6):
        chave = str(input(f'Digite a chave da sua {i}º cor: '))
        valor = str(input(f'Digte o valor da sua {i}º cor: '))
        print('-'*79)
        
        # Processamento de dados:
        cor.clear()
        cor[chave] = valor
        cores.append(cor.copy())
    
    # Impressão do dicionário informado pelo usuário:
    print('='*79)
    for cor in cores:
        for chave,valor in cor.items():
            print(f'{chave} : {valor}')
    print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)