# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 11/07/2024.
# Autor: Brendon João Campos Neves.
# C) Crie uma função que verifica se um aluno está cadastrado
# ou não em um dicionário. Se estiver cadastrado, imprima o nome desse aluno
# e o resto dos seus dados. O dicionário deverá conter nome,
# matrícula e a data de nascimento do aluno.

# Definindo funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cadastrar_aluno(nome='', matricula=0, nascimento='00/00/0000'):
    aluno = {}
    aluno[nome] = nome
    aluno['matricula'] = matricula
    aluno['nascimento'] = nascimento

    return aluno


def esta_cadastrado(lista_dicionarios, procurar=''):
    nao_encontrado = True
    if lista_dicionarios:
        for dicionario in lista_dicionarios:
            if procurar in dicionario.keys():
                nao_encontrado = False
                del dicionario[procurar]
                dicionario['nome'] = procurar
                for chave, valor in dicionario.items():
                    print(f'{chave}: {valor}')
            else:
                if nao_encontrado:
                    print('Aluno não encontrado!')
                    nao_encontrado = False


# Declarações de variáveis:
escola = []
aluno = {}
opcao = ''
nome = ''
matricula = 0
nascimento = ''

limpar_terminal()

print('.'*79)
print('Cadastrar e procurar aluno: ')
print('.'*79)

# Entrada de dados:
while True:
    print('.'*79)
    print('Comandos:')
    print('0 - Sair')
    print('1 - Cadastrar aluno')
    print('2 - Encontrar aluno')
    print('.'*79)

    opcao = int(input('Digite o nº da opção que deseja: '))
    if opcao == 0:
        break
    elif opcao == 1:
        nome = str(input('Digite o nome do seu aluno: '))
        matricula = int(input('Digite o nº de matrícula do aluno: '))
        nascimento = str(
            input('Digite a data de nascimento do aluno (00/00/0000): '))
        aluno.clear()
        aluno = cadastrar_aluno(
            nome=nome, matricula=matricula, nascimento=nascimento)
        escola.append(aluno.copy())
    elif opcao == 2:
        if escola:
            aluno_procurar = str(
                input('Digite o nome do aluno que deseja encontrar: ')).strip()
            esta_cadastrado(escola, procurar=aluno_procurar)
        else:
            print('Cadastre algum aluno antes de procura-lô!')
    else:
        print('Opção inválida!')

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
