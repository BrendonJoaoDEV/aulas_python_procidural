# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 16/06/2024.
# A) Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair).

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
entrada = ''
notas = []

# Imprimindo o título:
print('.'*79)
print('ARMAZENANDO NOTAS DE ALUNOS')
print('PRESSIONE "s" OU "0" PARA SAIR')
print('.'*79)

# Entrada de dados:
while True:
    entrada = input('Digite a nota do aluno: ')
    if ((entrada == 's') or (entrada == '0')):
        break
    else:
        notas.append(int(entrada))
        continue

# Saída de dados:
print('='*79)
print(f'Lista de notas dos alunos: {notas}')
print('='*79)

# Imprimindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)