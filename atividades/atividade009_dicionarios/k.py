# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 04/07/2024.
# K) Faça um programa que peça continuamente o nome e a idade de uma pessoa.
# Caso o usuário digite a idade 999, o programa será finalizado e executará uma impressão com os nomes cadastrados.

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('cls')

# Declarações de variáveis:
sociedade = []
pessoa = {}
nome = ''
idade = ''

# Impressão do título:
print('.'*79)
print('Jogo: Fuja do looping!')
print('.'*79)

# Entrada de dados:
print('-'*79)
while True:
    nome = str(input('Digite seu nome: '))
    idade = str(input('Digite sua idade: '))
    if idade == '999':
        pessoa.clear()
        pessoa[nome] = idade
        sociedade.append(pessoa.copy())
        break
    else:
        pessoa.clear()
        pessoa[nome] = idade
        sociedade.append(pessoa.copy())
        print('-'*79)
        continue

print('='*79)
print('Você escapou! Meus parabéns!')
print('='*79)
print('Nomes e idades que você tentou: ')
print('-'*79)
for pessoa in sociedade:
    for nome, idade in pessoa.items():
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print('-'*79)
print('='*79)

print('.'*79)
print('Fim do jogo! Obrigado ;)')
print('.'*79)