# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 17/06/2024.
# Desafio: Construa um código para exemplificar um CRUD. Não é permitido funções ou validações try exception.
# Prêmio: 1 cartela com 20 ovos (brancos)
# Em caso de empate, o prêmio será dividido.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
entrada = ''

# Exibindo título:
print('.'*79)
print('CRUD: Create, Read, Update e Delete.')
print('.'*79)

# Exibindo lista de comandos:
print('COMANDOS: ')
print('0 - sair')
print('1 - criar novo arquivo')
print('2 - exibir elementos de um arquivo')
print('3 - alterar um elemento de um arquivo')
print('4 - excluir um arquivo')

# Entrada de dados:
while True:
    print('-'*79)
    entrada = input('Digite o número correspondente a opção que deseja executar: ')
    print('-'*79)
    if entrada.isnumeric():
        entrada = int(entrada)
        # Processamento de dados:
        if entrada == 0:
            print('Saindo...')
            break
        elif entrada == 1:
            pass
        elif entrada == 2:
            pass
        elif entrada == 3:
            pass
        elif entrada == 4:
            pass
        else:
            print('Opção inválida! Digite o número correspondente a um dos comandos!')
            continue

# Fim do sistema:
print('.'*79)
print('Fim do sistema! Obrigado!')
print('.'*79)