# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/06/2024.
# B) Evolua o programa anterior para um código que pergunte ao usuário
# qual o intervalo que ele deseja ver impresso.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo o título.
print('.'*79)
print('INTERVALO DE NÚMEROS')
print('.'*79)

# Entrada de dados.
while True:
    print('-'*79)
    inicio = input('Digite o início do seu intervalo: ')
    final = input('Digite o final do seu intervalo: ')
    print('-'*79)

    # Validação de entrada.
    if not(inicio.isnumeric() and final.isnumeric()):
        print('Entrada inválida.')
        print('Por favor digite um número.')
    else:
        break
    
# Processamento/Saída de dados.
print('='*79)

for i in range(int(inicio), int(final)):
    print(i, end = ',')

print()
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)