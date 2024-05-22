# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 16/04/2024.
# Saída interpolada, formtada, f-string ou template string.

# Impotando as bibliotecas.
# Biblioteca para interagir com o SO.
import os
# Biblioteca para pegar data e hora do sistema.
import datetime  


# Limpando o terminal.
os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS EM PYTHON')
print('=' * 70)

# Entrada.
nome = input('Entre com um nome: ')
peso = input('Entre com o peso: ')
altura = input('Entre com a altura: ')

# Entrada com  Casting.
nascimento = int(input('Data de nascimento: '))
cep = int(input('Entre com o seu CEP: '))
bairro = str(input('Entre com o bairro: '))
rua = str(input('Nome da Rua: '))
numero = int(input('Entre com o número: '))

# Processamento: Pegando o ano corrente.
ano_atual = datetime.datetime.now() .year
idade = int(ano_atual) - nascimento

# Saída.
print('-' * 70)
print('SAÍDA DE DADOS')
print('=' * 70)
print('Nome: ', nome)
print('Data de nascimento: ', nascimento)
print('Peso: ', peso)
print('Altura: ', altura)

# Saída interpolada.
print(f'{nome}, você tem {idade} anos!')
print(f'CEP: {cep}')
print(f'Bairro: {bairro}')
print(f'Rua: {rua}')
print(f'Número: {numero}')
print('-' * 70)
print('')
