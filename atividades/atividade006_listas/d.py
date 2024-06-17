# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 16/06/2024.
# D) Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
entrada = ''
notas = []
soma = 0 + 0
media = 0

# Imprimindo o título:
print('.'*79)
print('MÉDIA ENTRE NOTAS DOS ALUNOS')
print('.'*79)


# Entrada de dados:
print('-'*79)
while True:
    entrada = input('Digite as notas de quatro alunos separadas por espaços: ')
    notas = entrada.split()
    # Validação de entrada:
    if (len(notas) > 4):
        print('Por favor insira apenas quatro notas!')
        continue
    else:
        break
    
print('-'*79)

# Processamento de dados:
for nota in notas:
    soma += int(nota)
media = soma / len(notas)

# Saída de dados:
print('='*79)
print(f'A média das notas {notas} é: {media}')
print('='*79)

# Imprimindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)