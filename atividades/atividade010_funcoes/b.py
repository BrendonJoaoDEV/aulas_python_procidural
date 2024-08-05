# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 11/07/2024.
# Autor: Brendon João Campos Neves.
# B) Crie uma função que cadastre o nome de um aluno, a matrícula e
# a data de nascimento. Depois imprima os resultados cadastrados
# utilizando uma estrutura de repetição for.

# Definições de funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cadastrar_aluno(nome='', matricula=0, nascimento='00/00/0000'):
    aluno = {}
    aluno['nome'] = nome
    aluno['matricula'] = matricula
    aluno['nascimento'] = nascimento
    
    return aluno


# Declarações de variáveis:
nome = ''
matricula = 0
nascimento = ''
aluno = {}
escola = []
opcao = ''

print('.'*79)
print('Cadastrar alunos: ')
print('.'*79)

# Entrada de dados:
print('-'*79)
while True:
    nome = str(input('Digite o nome do aluno: ')).strip()
    matricula = int(input('Digite o número de matrícula do aluno: '))
    nascimento = str(input('Digite a data de nascimento do aluno (00/00/0000): '))
    aluno.clear()
    aluno = cadastrar_aluno(nome=nome, matricula=matricula, nascimento=nascimento)
    escola.append(aluno.copy())
    
    opcao = str(input('Deseja adicionar outro aluno? (s/n)')).strip().lower()
    print('~'*79)
    if opcao == 's':
        continue
    else:
        print('-'*79)
        break

# Saída de dados:
print('='*79)
print('Alunos da escola: ')
for aluno in escola:
    for chave, valor in aluno.items():
        print(f'{chave}: {valor}')
    print('~'*79)
print('='*79)

# Aviso de fim:
print('.'*79)
print('Fim do progrma! Obrigado ;)')
print('.'*79)