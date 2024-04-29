# Curso de Desenvolvimento de Sistemas - SENAC.
# Turma: 0152. 
# Autor: Brendon João Campos Neves.
# Data: 29/04/2024.
# F) A empresa "LeapYearCheck" está desenvolvendo um software de verificação de anos bissextos para auxiliar usuários na identificação desses anos de forma rápida e precisa.
# Eles precisam de um programa que permita aos usuários inserir um ano e, em seguida, determine se esse ano é bissexto ou não, de acordo com as regras estabelecidas pelo calendário gregoriano.
# Além disso, é necessário realizar a validação de entrada de dados para garantir que o ano inserido pelo usuário seja um valor válido, ou seja, um número inteiro positivo.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*70)
print('Sistema da Leap Year Check')
print('Verificar se o ano é bissexto')
print('.'*70)

# Entrada de dados/Declaração de variáveis.
print('-'*70)
ano = float(input('Digite o ano que você deseja saber se é bissexto: '))
resposta = ''
print('-'*70)

# Processamento.
# Trocar tipo da variável ano(casting) para garantir que seja um inteiro.
ano = int(ano)
# Condicional:
# if(verifica se o ano inserido pelo usuário é igual ou menor a zero).
# Se sim mostra ao usuário umamensagem pedindo para digitar um ano válido.
# elif(verifica se o resto da divisão do ano inserido pelo usuário dividido por quatro é igual a zero).
# se sim o ano é bissexto.
# else(caso contrário).
# O ano não é bissexto.
if ano <= 0:
    resposta = (f'{ano} não é um ano válido por favor insira '
    + f'um ano diferente de zero, inteiro e positivo.')
elif ano % 4 == 0:
    resposta = f'O ano {ano} é um ano bissexto!'
else:
    resposta = f'O ano {ano} não é um ano bissexto'
    
# Saída.
print('='*70)
print(resposta)
print('='*70)

# Título de fim.
print('.'*70)
print('Fim do programa!')
print('.'*70)
print()