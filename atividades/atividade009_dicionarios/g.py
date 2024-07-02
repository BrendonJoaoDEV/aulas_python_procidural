# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/07/2024.
# G) Faça um programa para cadastrar os alunos de uma escola.
# Para os campos, tome como referência o nome do aluno, data de nascimento e matrícula.

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('cls')

# Declarações de variáveis:
escola = []
aluno = {}
nome = ''
nascimento = ''
matricula = ''
opcao = ''

# Impressão do título:
print('.'*79)
print('Cadastro de alunos:')
print('.'*79)

# Entrada de dados:
print('-'*79)
while True:
    nome = str(input('Digite o nome do aluno: ')).capitalize().strip()
    nascimento = str(input('Digite a data de nascimento do aluno: ')).strip()
    matricula = str(input('Digite o nº de matrícula do seu aluno: ')).strip()
    
    # Processamento de dados:
    aluno.clear()
    aluno['nome'] = nome
    aluno['nascimento'] = nascimento
    aluno['matricula'] = matricula
    escola.append(aluno.copy())
    
    # Escolha para adicionar outro aluno ou parar o sistema:
    opcao = str(input('Deseja adicionar outro aluno (s/n): ')).lower().strip()
    if opcao == 's':
        continue
    else:
        break

# Saída de dados:
print('='*79)
print('Alunos na escola:')
for aluno in escola:
    for chave, valor in aluno.items():
        print(f'{chave}: {valor}')
    print('-'*79)
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)