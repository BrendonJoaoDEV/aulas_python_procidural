# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 10/05/2024.
# f) Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

# Importando as bibliotecas.
import os
import random


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*79)
print('Jogo de adivinhação')
print('adivinhe o número de 1 a 10 que o sistema está pensando')
print('.'*79)

# Entrada.
print('-'*79)
chute = int(input('Digite o número que você acha que o sistema pensou: '))
print('-'*79)

# Declarações de variáveis.
numero = random.randint(1, 10)
resposta = ''

# Processamento.
if chute == numero:
    resposta = (f'Parabéns você acertou! '
    f'O número pensado pelo sistema e seu chute foram {numero}')
else:
    resposta = (f'Você errou! O número que o sistema pensou '
                f'foi {numero} e seu chute foi {chute}')

# Saída.
print('='*79)
print(resposta)
print('='*79)

# Título de fim.
print('.'*79)
print('Fim do jogo ;)')
print('.'*79)