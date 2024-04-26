# Curso de Desenvolvimento de Sitemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 25/04/2024.
# A) A empresa "TechSolutions" contratou você para desenvolver um programa em Python que irá automatizar uma parte do seu sistema de processamento de dados.
# Eles precisam de um programa que solicite ao usuário a entrada de um número inteiro e, em seguida, verifique se esse número é par ou ímpar.
# Essa funcionalidade é essencial para o sistema deles, pois eles processam grandes conjuntos de dados e precisam classificar os números de forma eficiente para realizar cálculos específicos em cada tipo de número.

# Importando as bivliotecas.
import os


# Limpando o terminal.
os.system('cls')

# Título
print('.'*70)
print('Sistema Tech Solutions')
print('Verifica se o número é par ou ímpar')
print('.'*70)

# Entrada/Declaração de variáveis.
print('-'*70)
numero = int(input('Digite um número inteiro: '))
resposta = ''
print('-'*70)

# Processamento
# Condicional para verificar se o número é par ou ímpar.
if numero % 2 == 0:
    resposta = f'O número {numero} é par'
else:
    resposta = f'O número {numero} é ímpar'

# Saída
print('='*70)
print(resposta)
print('='*70)
    
print('.'*70)
print('Fim do programa!')
print('.'*70)