# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/06/2024.
# E) Faça um programa que some a quantidade de números pares 
# encontrados no intervalo entre 0 e 100.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('QUANTOS Nº PARES EXISTEM ENTRE 0 E 100?')
print('.'*79)

# Declaração de variáveis.
contador = 0

# Somando os números e imprimindo o resultado.
print('='*79)

for i in range(0, 101, 2):
    contador += 1

print(f'Existem {contador} números pares no intervalo de 0 a 100.')
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)