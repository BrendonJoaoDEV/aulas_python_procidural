# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 23/05/2024.
# I) Faça um programa que receba o nome completo de uma pessoa e,
#  em seguida, mostre o primeiro e o último nome.

# Importando as bibliocas.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo o título.
print('.'*79)
print('Dividindo nome')
print('.'*79)

# Entrada de dados.
print('-'*79)
nome_completo = str(input('Digite seu nome completo: '))
print('-'*79)

# Declaração de variáveis.
erro = ''
lista_nomes = []
nome_minusculo = ''
primeiro_nome = ''
ultimo_nome = ''

# Validação.
if nome_completo == '':
    print('.'*79)
    erro = 'Você não digitou um nome.'
    print(erro)
    print('.'*79)
else:
    print('='*79)
    print(f'Seu nome completo é: {nome_completo}')

# Processamento de dados.
nome_minusculo = nome_completo.lower()
lista_nomes = nome_minusculo.split(' ')
primeiro_nome = lista_nomes[0]
ultimo_nome = lista_nomes[-1]
primeiro_nome = primeiro_nome.capitalize()
ultimo_nome = ultimo_nome.capitalize()

# Saída de dados.
print(f'Seu primeiro nome é: {primeiro_nome}.')
print(f'Seu último nom é: {ultimo_nome}.')
print('='*79)

# Título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)