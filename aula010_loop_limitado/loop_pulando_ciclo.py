# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 28/05/2024.
# for... range... continue.

import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE: CONTINUE')
print('='*70)

print()

for c in range(1, 11):
    if c == 5:
        # 5 está fora do loop, se retirar a linha abaixo,
        # ele não aparecerá na saída, deixei para verificação!
        print(f'O número {c} está fora do loop')
        continue     # Salta o ciclo e continua.
    
    
    print(f'O número é {c}')

print('-'*70)
print()