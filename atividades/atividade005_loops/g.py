# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 02/06/2024.
# G) Faça um programa que calcule os números primos em um 
# intervalo pré-determinado pelo usuário.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('NÚMEROS PRIMOS')
print('.'*79)

# Entrada de dados.
while True:
    print('-'*79)
    inicio = input('Digite o início do seu intervalo: ')
    final = input('Digite o final do seu intervalo: ')
    print('-'*79)
    
    # Validação da entrada.
    if not(inicio.isnumeric() and final.isnumeric()):
        print('Entrada inválida.')
        print('Por favot digite um número.')
    elif int(inicio) < 2:
        inicio = 2
        break
    else:
        break

# Declarações de variáveis.
primo = bool

# Processamento de dados.
print('='*79)
print(f'Os nº primos no intervalo de {inicio} a {final} são:')

for i in range(int(inicio), int(final) + 1):
    for i2 in range(int(inicio), i):
        if i % i2 == 0:
            break
    else:
        print(i, end = ', ')

print()
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)