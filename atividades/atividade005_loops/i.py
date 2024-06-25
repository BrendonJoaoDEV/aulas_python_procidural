# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 03/06/2024.
# I) Faça um algoritmo que imprima a frase "estou em looping" e, em seguida,
# solicite ao usuário digitar uma letra. Caso a letra seja o “f" finalize a aplicação.
# Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo o título.
print('.'*79)
print('JOGO DE ADIVINHAÇÃO')
print('Adivinhe a letra e salve o sistema!')
print('.'*79)

# Imprimindo mensagem do sistema.
print('-'*79)
print('Estou em looping! Por favor me ajude!')
print('-'*79)

# Pedindo para o usuário chutar uma letra.
while True:
    print('-'*79)
    chute = input('Digite uma letra para tentar salvar o sistema: ').lower()
    print('-'*79)
    if (chute == 'f'): # Se o usuário chutar f.
        print('='*79)
        print('Parábens você conseguiu salvar o sistema!') # Exibir mensagem de parabenização.
        print('='*79)
        break # E parar o looping.

# Imprimindo título de fim.
print('.'*79)
print('Fim do Jogo! Obrigado!')
print('.'*79)
