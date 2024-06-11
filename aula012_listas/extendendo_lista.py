# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 10/06/2024.
# Estrutura de dados: Listas [] + append() + extend().

import os


os.system('cls')

# Inicializa a lista vazia.
lista_numeros = []

# Solicita ao usuátio para inserir números separados por espaço.
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings.
numeros = entrada.split()

# Cria uma lista para armazenar os números pares.
pares = []

# Itera sobre os números inseridos.
for numero in numeros:
    # Converte a string para inteiro.
    numero_aux = int(numero)
    # Verifica se o número é par.
    if numero_aux % 2 == 0:
        # Adiciona o número par à lista de pares.
        pares.append(numero_aux)

# Usa extend() para adicionar todos os números pares à lista principal.
lista_numeros.extend(pares)

# Exibe a lista resultante.
print(f'Números pares adicionados à lista: {lista_numeros}')