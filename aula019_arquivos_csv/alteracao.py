# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 15/08/2024.
# Desafio: Fazer alteração em arquivos csv.

# Importando as biblbiotecas:
import csv
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
arquivo = 'aula019_arquivos_csv/gravacao/alunas.csv'
nome_alterar = ''
pessoa_alterar = {}
cadastro = []
registro = {}
nao_existe = True

# Lendo o arquivo:
with open(arquivo, 'r') as arquivo_csv:
    # Objeto que lê o arquivo existente.
    leitor = csv.DictReader(arquivo_csv, delimiter=';')
    # Salvando o que foi lido como uma lista de dicionários:
    cadastro = list(leitor)

print('.'*79)
print('Alteração arquivo CSV')
print('.'*79)

# Perguntando ao usuário quem ele deseja alterar:
while nao_existe:
    nome_alterar = str(input('Digite o nome de quem deseja alterar: '))
    for registro in cadastro:
        if registro['nome'] == nome_alterar:
            nao_existe = False
            pessoa_alterar = registro
            del registro
            break
    else:
        print('Nome não encontrado no arquivo!')
        continue

print('='*79)
for k, v in pessoa_alterar.items():
    print(f'{k}: {v}', end=' ; ')
    print()
print('='*79)

# Perguntando o que o usuário deseja alterar:
print('-'*79)
while True:
    opcao = str(input('Qual informação deseja alterar? (nome/'
                    'telefone/cidade) ')).lower().strip()
    print('-'*79)
    
    if opcao == 'nome':
        novo_nome = str(input(f'Digite o novo nome de {nome_alterar}: '))
        for campo, dado in pessoa_alterar.items():
            if campo == 'nome':
                pessoa_alterar['nome'] = novo_nome
        break
    elif opcao == 'telefone':
        novo_telefone = str(input(f'Digite o novo telefone de {nome_alterar}: '))
        for campo, dado in pessoa_alterar.items():
            if campo == 'telefone':
                pessoa_alterar['telefone'] = novo_telefone
        break
    elif opcao == 'cidade':
        nova_cidade = str(input(f'Digite a nova cidade de {nome_alterar}: '))
        for campo, dado in pessoa_alterar.items():
            if campo == 'cidade':
                pessoa_alterar['cidade'] = nova_cidade
        break
    else:
        print('Opção inválida!')
        continue

with open(arquivo, 'w', newline='') as arquivo_csv:
    # Campos do arquivo:
    campos = ['nome', 'telefone', 'cidade']
    # Objeto qu escreve o arquivo:
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    # Escrevendo o cabeçalho:
    escrever.writeheader()
    # Escrevendo dados:
    escrever.writerows(cadastro)