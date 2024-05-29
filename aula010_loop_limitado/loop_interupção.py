# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 28/05/2024.
# for... range... break.

import os 


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE: BREAK')
print('='*70)

print()

for c in range(0, 10):
    
    print(f'Valor: {c}')
    
    # Condição para terminar a contagem.
    if (c == 5):
        print(f'Contagem interrompida no {c}')
        break

print('-'*70)
print('FIm do Programa!')
print()