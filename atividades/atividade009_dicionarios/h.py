# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/07/2024.
# H) Faça um programa para ler o dicionário nomes = {‘nome’: ’John, ‘idade’: 40, ‘peso’: 80, ‘altura’: 1.70}.
# Em seguida realize as seguintes ações:
# - Listar chaves e valores com laço - Deletar o peso
# - Listar novamente chaves e valores - mostrar o nome e altura

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('cls')

# Declarações de variáveis:
pessoa = {
    'nome' : 'John',
    'idade' : 40,
    'peso' : 80,
    'altura' : 1.70
}

# Impressão do título:
print('.'*79)
print('Processamento do dicionário:')
print('.'*79)

# Exibindo dicionário antes:
print('-'*79)
print('Dicionário:')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
print('-'*79)

# Processamento: Deletar o peso e exibir:
del pessoa['peso']
print('='*79)
print('Sem o peso:')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
print('='*79)

# Processamento: exibir apenas nome e altura:
del pessoa['altura']
print('='*79)
print('Apenas nome e altura:')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
print('='*79)