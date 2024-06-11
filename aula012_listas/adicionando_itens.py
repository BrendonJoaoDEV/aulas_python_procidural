# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 10/06/2024.
# Estrutura de dados: Listas [] + append().

import os


os.system('cls')

# Inicializa uma lista vazia.
lista_numeros = []

# Pede ao usuário para inserir três números.
for i in range(3):
    numero = int(input('Digite um número: '))
    
    # Adiciona o número à lista.
    lista_numeros.append(numero)

# Verifica se o número inserido está na lista e
# exibe uma mensagem correspondente.
numero_verificar = int(input('Digite um número: '))

if numero_verificar in lista_numeros:
    print(f'O número {numero_verificar} está na lista!')
else:
    print(f'O número {numero_verificar} não está na lista.')