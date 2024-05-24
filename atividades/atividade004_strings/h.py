# Curso de Desenvolvimento e Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 23/05/2024.
# H) Faça um programa que leia o nome de um aluno e,
# mostre quantas vezes a letra 'o' aparece e
# em que posição ela aparece pela primeira e última vez.

# Importando as bibliotecas.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('Letras o do nome do aluno')
print('.'*79)

# Entrada de dados.
print('-'*79)
nome = str(input('Digite seu nome: '))
print('-'*79)

# Declarações de variáveis.
erro = ''
nome_minusculo = ''
numero_o = ''
primeiro_o = ''
ultimo_o = ''

# Validação.
if nome == '':
    print('.'*79)
    erro = 'Você não inseriu um nome.'
    print(erro)
    print('.'*79)
else:
    print('='*79)
    print(f'Seu nome é: {nome}.')

# Processamento de dados.
nome_minusculo = nome.lower()
numero_o = nome_minusculo.count('o')
primeiro_o = nome_minusculo.find('o') + 1
ultimo_o = nome_minusculo.rfind('o') + 1

# Saída de dados.
print(f'A letra "o" apareceu: {numero_o}.')
print(f'Apareceu pela primeira vez no {primeiro_o}º caractere.')
print(f'E apareceu pela ultima vez no {ultimo_o}º caractere.')
print('='*79)

# Título fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)