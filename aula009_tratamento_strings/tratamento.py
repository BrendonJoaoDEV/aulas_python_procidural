# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 09/05/2024.
# Funções úteis para o tratamento de strings.

import os


os.system('cls')

print('-'*70)
print('Funções String')
print('='*70)

frase1 = 'Olá, Mundo!'
quantidade_caracteres = len(frase1) # Conta os caracteres.
print(f'A frase {frase1} \ncontém {quantidade_caracteres} caracteres')
print('.'*70)

minusculas = frase1.lower() # Frase em minúsculo.
print(f'Frase original: {frase1}')
print(f'Frase nova: {minusculas}')
print('.'*70)

maiusculas = frase1.upper() # Frase em maiúsculo.
print(f'Frase original: {frase1}')
print(f'Frase nova: {maiusculas}')
print('.'*70)

capitalizada = frase1.capitalize() # Frase capitalizada.
print(f'Frase original: {frase1}')
print(f'Frase nova: {capitalizada}')
print('.'*70)

frase2 = '   Olá, Mundo!   '
sem_espacos = frase2.strip() # Retirar espaços, antes e depois.
print(f'Frase original: {frase2}')
print(f'Frase nova: {sem_espacos}')
print('.'*70)

substituicao = frase1.replace('Mundo', 'Python') # Troca palavra.
print(f'Frase original: {frase1}')
print(f'Frase nova: {substituicao}')
print('.'*70)

lista = frase1.split(',') # Separa as palavras de uma str e, uma lista.
print(f'Frase original: {frase1}')
print(f'Frase nova: {lista}')
print('.'*70)

lista = ['Olá', 'mundo']
juncao = '-'.join(lista) # Transforma uma lista em uma string com separador.
print(f'Frase original: {lista}')
print(f'Frase nova: {juncao}')
print('.'*70)