# Trabalho sobre a estrutura de dados SET.
# Senac Minas Gerais/Juiz de Fora.
# Aluno: Brendon João Campos Neves.
# Turma: 0152.
# Ano: 2024

# Encontrar os elementos que estão em algum dos dois conjuntos mas não em ambos.

import os


os.system('cls')

# Declarações de variáveis:
entrada = ''
numero_elementos_set_1 = 0
conjunto_1 = []
numero_elementos_set_2 = 0

print('.'*79)
print('DIFERENÇA SIMÉTRICA')
print('.'*79)

numero_elementos_set_1 = int(
    input('Digite o nº de elementos que seu 1º conjunto terá: '))

for i in range(numero_elementos_set_1):
    entrada = conjunto_1.append(input(f'Digite o {i+1}º nº: '))

conjunto_1 = set(conjunto_1)


        