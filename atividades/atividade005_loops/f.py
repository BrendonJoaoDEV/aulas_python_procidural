# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/06/2024.
# F) Faça um programa que imprima os números primos entre 0 e 100.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('NÚMEROS PRIMOS ENTRE 0 E 100')
print('.'*79)

# Declarações de variáveis.
primos = [] # Lista que receberá os primos encontrados.

# Processamento dos números.
for i in range(2, 101): # For para gerar os números de 2 a 100.
    primo = True # Flag que afirma que o número é primo.
    for j in range (2, i): # For que gera os números de 2 a i.
        if i % j == 0: # Verifica se o nº i dividido por j gera o resto 0.
            primo = False # Se sim diz que não é primo.
            break # Para o looping pois o número não é primo.
    if primo: # Se primo ainda for True.
        primos += [i] # Adiciona i a lista de primos.

# Saída dos números primos encontrados.
print('='*79)
print(primos)
print('='*79)

# Imprimindo o título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)