# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 28/05/2024.
# while... if... else... continue...

import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE CONTINUE')
print('='*70)

print()

contador = 0 # Flag

while (contador <= 10):
    
    # Soma o contador.
    contador += 1 # É o mesmo que contador = Contador + 1.
    
    if (contador % 2 == 0): # Pulando os pares.
        continue
    print(f'Contador = {contador}')
else:
    print(f'Bloco do while...else: contador em {contador}!')

print('-'*70)
print('Fim do programa!')
print()