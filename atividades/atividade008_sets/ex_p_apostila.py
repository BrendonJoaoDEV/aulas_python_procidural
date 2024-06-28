# Trabalho sobre a estrutura de dados SET.
# Senac Minas Gerais/Juiz de Fora.
# Aluno: Brendon João Campos Neves.
# Turma: 0152.
# Ano: 2024

# Encontrar os elementos que estão em algum dos dois conjuntos mas não em ambos.

import os


os.system('cls')

# Declarações de variáveis:
conjunto_1 = set
conjunto_2 = set
diferenca_simetrica_1 = set
diferenca_simetrica_2 = set

print('.'*79)
print('DIFERENÇA SIMÉTRICA')
print('.'*79)

# Entrada:
print('-'*79)

while True:
    conjunto_1 = set(input('Digite seu 1º conjunto: '))
    conjunto_2 = set(input('Digite seu 2º conjunto: '))
    if conjunto_1 and conjunto_2: # Verifica se os conjuntos não estão vazios.
        break

print('-'*79)
# Processamento:
# Encontra os elementos que estão em algum dos dois conjuntos mas não em ambos.
diferenca_simetrica_1 = conjunto_1.symmetric_difference(conjunto_2) # Usando a função symmetric_difference().
diferenca_simetrica_2 = conjunto_1 ^ conjunto_2 # Usando o operador ^.


# Saída:
print('='*79)
print(f'Diferença simétrica usando função: ')
for numero in diferenca_simetrica_1:
    print(numero, end=', ')
print()
print('='*79)
print(f'Diferença simétrica usando operador: ')
for numero in diferenca_simetrica_2:
    print(numero, end=', ')
print()
print('='*79)

print('.'*79)
print('Fim do programa!')
print('.'*79)