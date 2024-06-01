# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/06/2024.
# A) Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo o título.
print('.'*79)
print('NÚMEROS DE 1 A 100')
print('.'*79)

# Imprimindo os números.
print('='*79)

for i in range(0, 100):
    print(i+1, end = ',')

print()
print('='*79)

# Imrpimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)