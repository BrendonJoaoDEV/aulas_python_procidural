# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 28/05/2024.
# while... if... else... break.

import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE BREAK')
print('='*70)

print()

while (True):
    
    # lower() garante o tratamento para entrada de 's' ou 'S'.
    nome = str(input('Digite um nome [s - sair]: ')).lower()
    
    if (nome != 's'):
        print('Continue digitando...')
    else:
        print('-'*70)
        print('Você digitou "s" para sair!')
        
        # Interrompe o laço.
        break

print('-'*70)
print()