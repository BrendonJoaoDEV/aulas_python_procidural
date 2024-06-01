# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/06/2024.
# F) Faça um programa que imprima os números primos entre 0 e 100.

# Importando as bibliotecas do sistema.
import os
import math


# Limpando o terminal.
os.system('clear')

# Imprimindo título.
print('.'*79)
print('NÚMEROS PRIMOS ENTRE 0 E 100')
print('.'*79)

# Gera o intervalo que será analisado.
for i in range(2, 101):
    # Flag que diz que o número é primo.
    is_prime = True
    # Verifica se o número é divisivel somente por 1 e por ele mesmo.
    for j in range(2, math.ceil(math.sqrt(i))):
        if i % i == 0:
            is_prime = False
            break
    # Se o número é primo, imprime
    if is_prime:
        print(i, end=" ")
