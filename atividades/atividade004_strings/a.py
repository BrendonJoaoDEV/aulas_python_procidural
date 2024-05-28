# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: brendon João Campos Neves.
# Data: 21/05/2024.
# A) Faça um programa que solicite separadamente o nome,
# o nome do meio e o sobrenome de uma pessoa.
# Em seguida, imprima o nome completo.

# Importando as bibliotecas.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo o título.
print('.'*79)
print('NOME COMPLETO')
print('.'*79)

# Entrada de dados.
print('-'*79)
nome = input('Digite seu 1ª nome: ')
nome_do_meio = input('Digite seu nome do meio: ')
sobrenome = input('Digite seu sobrenome: ')
print('-'*79)

# Processamento de dados.
lista_nomes = [nome, nome_do_meio, sobrenome]
lista_nomes_str = str(lista_nomes)
nome_completo = ' '.join(lista_nomes_str)

# Saída de dados.
print('='*79)
print(f'Seu nome completo é {nome_completo}')
print('='*79)

# Título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)