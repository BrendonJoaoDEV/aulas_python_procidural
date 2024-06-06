# Curso de Desenvolvimento de sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves
# Data: 05/06/2024.
# e) Faça um programa para sortear um número de 1 a 20.

# Importando as bibliotecas do sistema.
import os
import random


# Limpando o terminal.
os.system('cls')

# Declarações de variáveis.
aleatorio = 0

# Imprimindo título.
print('.'*79)
print('SORTEANDO UM NÚMERO DE 1 A 20')
print('.'*79)

# Processamento.
aleatorio = random.randint(1, 20)

# Saída de dados.
print('='*79)
print(f'O número sorteado foi: {aleatorio}')
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)