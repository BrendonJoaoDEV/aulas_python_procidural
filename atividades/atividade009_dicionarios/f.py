# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 01/07/2024.
# F) Faça um programa que cadastra 5 tipos de vinho.
# Para os campos deste cadastro tome como referência nome do vinho, tipo, teor alcoólico e safra.

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('cls')

# Declarações de variáveis:
adega = []
vinho = {}
nome = ''
tipo = ''
teor = ''
safra = ''

# Impressão do título:
print('.'*79)
print('Organização da adega de vinhos:')
print('.'*79)

# Entrada de dados:
print('-'*79)
print('Cadastro de vinhos:')
for i in range(1, 6):
    nome = str(input(f'Digite o nome do seu {i}º vinho: '))
    tipo = str(input(f'Digite o tipo do seu {i}º vinho: '))
    teor = str(input(f'Digite o teor alcoólico do seu {i}º vinho: '))
    safra = str(input(f'Digite a safra do seu {i}º vinho: '))
    print('-'*79)
    
    # Processamneto de dados:
    vinho.clear()
    vinho['nome'] = nome.strip()
    vinho['tipo'] = tipo.strip()
    vinho['teor'] = teor.strip()
    vinho['safra'] = safra.strip()
    adega.append(vinho.copy())

# Saída de dados:
print('='*79)
print('Vinhos na adega:')
for vinho in adega:
    for chave, valor in vinho.items():
        print(f'{chave}: {valor}')
    print('-'*79)
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)