# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 15/06/2024.
# C) Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12

# Importando as bibliotecas do sistema.
import os

# Limpando o terminal.
os.system('cls')

# Declarações de variáveis.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numero = 0
reversa = []
de1a9 = []
de8a13 = []
pares = []
impares = []
produto = 0 * 0
de5a6 = []
de11a12 = []
resultado = []
multiplos_2 = []
multiplos_3 = []
multiplos_4 = []

# Mostrando a lista ao usuário.
print('.'*79)
print(f'PROCENSANDO O INTERVALO {lista}')
print('.'*79)

# Processamento da lista
# Lista reversa.
reversa = lista.reverse()

# Intervalo de 1 a 9.
de1a9 = lista[1:10]

# Intervalo de 8 a 13.
de8a13 = lista[8:14]

# Números pares e ímpares.
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Produto dos intervalos 5-6 por 11-12.
de5a6 = lista[5:7]
de11a12 = lista[11:13]
for numero_a in de5a6:
    for numero_b in de11a12:
        produto = numero_a * numero_b
        resultado.append(produto)

