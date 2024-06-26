# Trabalho sobre a estrutura de dados SET.
# Senac Minas Gerais/Juiz de Fora.
# Aluno: Brendon João Campos Neves.
# Turma: 0152.
# Ano: 2024

# Encontrar os elementos que estão em algum dos dois conjuntos mas não em ambos.

import os


os.system('cls')

# Declarações de variáveis:
entrada_1 = ''
entrada_2 = ''
conjunto_1 = set()
conjunto_2 = set()


print('.'*79)
print('DIFERENÇA SIMÉTRICA')
print('.'*79)

# Entrada:
print('-'*79)
print('DIGITE OS ELEMENTOS DO SEU CONJUNTO SEPARADOS POR ESPAÇOS')
while True:
    entrada_1 = input('Digite o 1º conjunto: ').split(' ')
    for elemento in entrada_1:
        if (elemento.isdigit()):
            conjunto_1.add(int(elemento))
        else:
            print('Entrada inválida! Digite apenas números!')

# Processamento:

# Saída:

print('.'*79)
print('Fim do programa!')
print('.'*79)