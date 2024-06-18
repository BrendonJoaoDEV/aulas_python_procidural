# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 17/06/2024.
# E) Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declara~ções de variáveis:
nomes_chutes = ''
nome_sistema = 'Pedro'
chutes = []
resposta = ''

# Exibindo o título:
print('.'*79)
print('JOGO: ADIVINHE O NOME DO SISTEMA')
print('.'*79)

# Entrada de dados:
while True:
    nomes_chutes = input('Digite 6 nomes separados por espaços: ')
    chutes = nomes_chutes.split()

    # Validações de dados:
    if (len(chutes) > 6):
        print('Digite apenas seis nomes!')
        continue

    # Processamento de dados:
    elif nome_sistema in chutes:
        resposta = f'Parabéns você acertou! O nome do sistema é {nome_sistema}'
        break
    else:
        print(f'Você errou! Tente novamente!')
        continue

# Saída de dados:
print('='*79)
print(resposta)
print('='*79)

# Exibindo título de fim:
print('.'*79)
print('Fim do jogo! Obrigado por jogar!')
print('.'*79)
