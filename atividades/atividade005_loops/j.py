# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 03/06/2024.
# J) Crie um programa que realiza a contagem de 1 até 100,
# usando apenas de números ímpares,ao final do processo exiba na tela quantos números ímpares foram
# encontrados nesse intervalo, assim como a soma dos mesmos.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('NÚMEROS ÍMPARES DE 0 A 100')
print('.'*79)

# Declarações de variáveis.
contagem = 0
impares = 0

# Contando de 0 a 100.
for i in range(0, 101):
    if (i % 2 != 0):
        contagem += 1
        impares += i
    else:
        continue

# Saída de dados.
print('='*79)
print(f'Entre 0 e 100 existem {contagem} nº ímpares,')
print(f'E a soma de todos eles é {impares}.')
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do Porgrama! Obrigado!')
print('.'*79)