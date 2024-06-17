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

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
reversa = []
de1a9 = []
de8a13 = []
pares = []
impares = []
multiplos_2 = []
multiplos_3 = []
multiplos_4 = []
produtos_intervalos = []
produto = 0 * 0
numero_a = 0
numero_b = 0

# Título:
print('.'*79)
print(f'PROCESSANDO LISTA: {lista}')
print('.'*79)

# Processamentos:
# Gerando e armazenando o intervalo de 1 até 9:
de1a9 = lista[0:9]

# Gerando e armazenando o intervalo de 8 até 13:
de8a13 = lista[7:13]

# Gerando e armazenando a lista reversa:
reversa = lista.copy()
reversa.reverse()

# Gerando e armazenando os números pares e ímpares:
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Multiplos de 2:
for numero in lista:
    if numero % 2 == 0:
        multiplos_2.append(numero)
    else:
        continue
    
# Multiplos de 3:
for numero in lista:
    if numero % 3 == 0:
        multiplos_3.append(numero)
    else:
        continue

# Multiplos de 4:
for numero in lista:
    if numero % 4 == 0:
        multiplos_4.append(numero)
    else:
        continue

# Produto dos intervalos 5-6 por 11-12:
for numero_a in lista[4:6]:
    for numero_b in lista[10:12]:
        produto = numero_a * numero_b
        produtos_intervalos.append(produto)


# Saída:
print('='*79)
print(f'Lista reversa: {reversa}')
print(f'Intervalo de 1 até 9: {de1a9}')
print(f'Intervalo de 8 até 13: {de8a13}')
print(f'Números pares na lista: {pares}')
print(f'Números ímpares na lista: {impares}')
print(f'Números multiplos de 2: {multiplos_2}')
print(f'Números multiplos de 3: {multiplos_3}')
print(f'Números multiplos de 4: {multiplos_4}')
print(f'Produto dos intervalos 5-6 por 11-12: {produtos_intervalos}')
print('='*79)

# Título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)