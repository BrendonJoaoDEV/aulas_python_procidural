# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 11/06/2024.
# Estrutura de dados: Listas [] + reverse() para inverter os elementos da lista sem alterar sua ordem.

import os


os.system('cls')

# Solicita ao usuário para inserir números separados por espaço.
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings.
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros.
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Exibe a lista fornecida para referência.
print('Lista fornecida: ', numeros)

# Solicita ao usuário para decidirse deseja inverter a lista.
escolha = input('Deseja inverter a ordem da lista? (s/n): ').strip().lower()

# Verifica a escolha do usuário e inverte a lista se a resposta for 's'.
if escolha == 's':
    numeros.reverse()
    print('Lista invertida: ', numeros)
else:
    print('A lista não foi invertida.')
