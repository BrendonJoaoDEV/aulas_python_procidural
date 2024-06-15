# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 15/06/2024.
# B) Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('SOMANDO ELEMENTO DE UMA LISTA')
print('.'*79)

# Declarações de variáveis
numero_entrada = 0
numero = 0
numeros = []
soma = 0 + 0

# Entrada de dados do usuário.
print('-'*79)

while True:
    numero_entrada = input('Digite um número: ')
    # Validação de dados.
    if (numero_entrada.isnumeric()):
        numero_entrada = int(numero_entrada)
        numeros.append(numero_entrada)
        if (len(numeros) == 5):
            break
    else:
        print('Entrada inválida!')
        continue

print('-'*79)

# Processamento de dados.
for numero in numeros:
    soma += numero

# Saída de dados.
print('='*79)
print(f'Sua sequência de números: {numeros}')
print(f'A soma de todos os elementos dessa sequência é: {soma}')
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)
