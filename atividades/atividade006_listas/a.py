# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 12/06/2024.
# # A) Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Declarações de variáveis.
lista = [1, 2, 3, 5, 6]
elemento = ''
posicao = ''

# Imprimindo título.
print('.'*79)
print('JOGO: COMPLETE A SEQUÊNCIA')
print('.'*79)

# Mostrando ao usuário a sequência atual.
print(F'Sequência atual: {lista}')
print('.'*79)

# Entrada do usuário.
print('-'*79)

while True:
    elemento = input('Digite o número que deseja inserir: ')
    posicao = input(f'Digite a posição que deseja inserir o nº {elemento}: ')
    # Validação da entrada do usuário.
    if (elemento.isnumeric() and posicao.isnumeric()):
        elemento = int(elemento)
        posicao = int(posicao) - 1
        # Processamento da entrada.
        if (posicao == 3 and elemento == 4):
            lista.insert(posicao, elemento)
            break
        else:
            print('Número ou posição incorretos!')
            print('Por favor tente novamente!')
            continue
    else:
        print('Número ou posição inválidos!')
        print('Insira apenas números!')
        continue

print('-'*79)

# Resultado da sequência (Saída de dados).
print('='*79)
print(f'Resultado da sequência: {lista}')
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Obrigado por jogar! Meus parabéns!')
print('.'*79)
