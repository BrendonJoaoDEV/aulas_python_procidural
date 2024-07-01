# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 30/06/2024.
# A) Faça um programa para criar um dicionário com 4 elementos.

# Importação de bibliotecas:
import os


# Limpeza do terminal: 
os.system('cls')

# Declarações de variáveis:
dicionarios = []
dicionario = {}
chave = ''
valor = ''

# Impressão do título:
print('.'*79)
print('Estrutura de dados: Dicionário')
print('.'*79)

# Entrada de dados:
print('-'*79)
for i in range(1, 5):
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

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)