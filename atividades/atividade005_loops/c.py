# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/06/2024.
# C) Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo o título.
print('.'*79)
print('CONTAGEM REGRESSIVA')
print('.'*79)

# Imprimindo os números em ordem decrescente.
print('='*79)

for i in range(10, 0, -1):
    print(f'Contando...{i}.')

print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)