# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 05/08/2024.
# Autor: Brendon João Campos Neves.
# H) Uma Academia deseja fazer uma pesquisa entre
# seus clientes para descobrir a média de altura
# e peso de seus clientes. Faça um programa que pergunte
# a cada um dos clientes da academia
# seu código, nome, altura e peso. Após esse cadastramento,
# seu programa deverá listar os dados dos clientes
# e a média. Para sair do programa o usuário deverá digitar
# o valor zero(0).
# O número de clientes é indefinido. Veja a saída no próximo slide.

# Definindo funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cadastrar(academia):
    codigo = input('Digite seu código: ')
    nome = input('Digite seu nome: ')
    altura = input('Digite sua altura: ')
    peso = input('Digite seu peso: ')
    cliente = {
        'Código': codigo,
        'Nome': nome,
        'Altura': float(altura),
        'Peso': float(peso)
    }
    academia.append(cliente)
    return academia


def calcular_media(academia):
    peso_total = 0
    altura_total = 0
    pessoas_peso = 0
    pessoas_altura = 0
    
    for cliente in academia:
        if (cliente['Peso']):
            peso_total += cliente['Peso']
            pessoas_peso += 1

        if (cliente['Altura']):
            altura_total += cliente['Altura']
            pessoas_altura += 1

    media_peso = peso_total / pessoas_peso
    media_altura = altura_total / pessoas_altura

    return media_peso, media_altura


# Declarações de variáveis:
academia = []
cliente = {}
opcao = ''
media_peso = 0
media_altura = 0

print('.'*79)
print('Pesquisa na academia')
print('.'*79)

print('-'*79)
while True:
    print('0 - Sair')
    print('1 - Participar')
    print('2 - Visualiza media atual')
    print('-'*79)
    opcao = input('Digite a opção desejada: ')
    if (opcao == '0'):
        break
    elif (opcao == '1'):

        # Entrada de dados:
        cadastrar(academia)
        print('-'*79)
    elif (opcao == '2'):

        # Processamento de dados:
        media_peso, media_altura = calcular_media(academia)

        # Saída de dados:
        print('='*79)
        print(f'A média de peso é: {media_peso: .2f}')
        print(f'A média de altura é: {media_altura: .2f}')
        print('='*79)

print('-'*79)

# Saída de dados(fim da pesquisa):
print('='*79)
print('Participantes:')
for cliente in academia:
    for chave, valor in cliente.items():
        print(f'{chave}: {valor}')
    print('-'*79)
print('='*79)
print('Resultados finais:')
print(f'A média de peso é: {media_peso: .2f}')
print(f'A média de altura é: {media_altura: .2f}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
