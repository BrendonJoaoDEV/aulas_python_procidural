# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 16/06/2024.
# G) Ler uma lista com 10 números, depois apresente o maior e o menor número da lista.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
entrada = ''
numeros_str = []
numeros_int = []
numero = 0
maior = int
menor = int

# Imprimindo título:
print('.'*79)
print('ENCONTRANDO O MAIOR E MENOR NÚMEROS')
print('.'*79)

# Entrada de dados:
print('-'*79)
while True:
    entrada = input('Digite 10 números separados por espaços: ')
    numeros_str = entrada.split()
    
    # Validação de dados:
    # Verifica se existem menos de 10 números na entrada do usuário.
    if (len(numeros_str) > 10):
        print('Digite no máximo 10 números!')
        continue
    
    # Verifica se o usuário entrou apenas com números.
    for numero in numeros_str:
        if (numero.isnumeric()):
            numeros_int.append(int(numero))
        else:
            print('Digite apenas números!')
            break
    # Se sim finaliza a entrada.
    else:
        break
print('-'*79)

# Processamento de dados:
maior = numeros_int[0]
for numero in numeros_int:
    if numero > maior:
        maior = numero
    else:
        continue

menor = numeros_int[0]
for numero in numeros_int:
    if numero < menor:
        menor = numero
    else:
        continue

# Saída de dados:
print('='*79)
print(f'Seu intervalo: {numeros_int}')
print(f'Nesse intervalo o maior número é {maior}')
print(f'E o menor número é {menor}')
print('='*79)

# Imprimindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)