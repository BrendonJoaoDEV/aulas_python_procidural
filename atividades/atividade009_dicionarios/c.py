# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 30/06/2024.
# C) Utilizando o exercício anterior, retire um elemento do dicionário.

# Importação de bibliotecas:
import os


# Limpeza do terminal: 
os.system('cls')

# Declarações de variáveis:
dicionarios = []
dicionario = {}
chave = ''
valor = ''
apagar = ''

# Impressão do título:
print('.'*79)
print('Estrutura de dados: Dicionário')
print('.'*79)

# Entrada de dados:
print('-'*79)
for i in range(1, 7):
    chave = str(input(f'Digite a chave do seu {i}º elemento: '))
    valor = str(input(f'Digite o valor do seu {i}º elemento: '))
    print('-'*79)
    
    # Processamento de dados: 
    dicionario.clear()
    dicionario[chave] = valor
    dicionarios.append(dicionario.copy())

# Saída de dados:
print('='*79)
for dicionario in dicionarios:
    for chave, valor in dicionario.items():
        print(f'{chave} : {valor}')
print('='*79)

# Pedindo ao usuário para selecionar o elemento que será apagado:
print('-'*79)
apagar = str(input('Digite a chave do elemento que deseja apagar: '))
print('-'*79)

for dicionario in dicionarios:
    if apagar in dicionario:
        del dicionario[apagar]
        
# Saída de dados depois do item removido:
print('='*79)
for dicionario in dicionarios:
    for chave, valor in dicionario.items():
        print(f'{chave} : {valor}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)