# Trabalho sobre a estrutura de dados SET.
# Senac Minas Gerais/Juiz de Fora.
# Aluno: Brendon João Campos Neves.
# Turma: 0152.
# Ano: 2024

# Encontrar os elementos que estão em algum dos dois conjuntos mas não em ambos.

import os


os.system('cls')

# Declarações de variáveis:
flag = True
conjunto_1 = set()
conjunto_2 = set()
diferença_simetrica = []

print('.'*79)
print('DIFERENÇA SIMÉTRICA')
print('.'*79)

# Entrada:
print('-'*79)
while flag:
    conjunto_1.add(input('Digite seu 1º conjunto: '))
    conjunto_2.add(input('Digite seu 2º conjunto: '))
    for elemento in conjunto_1:
        if (not(elemento.isdigit())):
            break
    else:
        flag = False
        continue
    for elemento in conjunto_2:
        if (not(elemento.isdigit())):
            break
    else:
        flag = False
        continue
    break
                

# Processamento:

# Saída:

print('.'*79)
print('Fim do programa!')
print('.'*79)