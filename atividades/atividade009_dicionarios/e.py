# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 30/06/2024.
# E) Faça um programa para criar um dicionário com 5 ferramentas.
# Depois, imprima os valores e a quantidade de elementos do dicionário.

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('cls')

# Declarações de variáveis:
ferramentas = {
    'Parafuso' : 'Chave Philips',
    'Porca' : 'Chave de boca',
    'Tábua' : 'Serrote',
    'Parede' : 'Furadeira',
    'Prego' : 'Martelo'
    
}

ferramenta = {}

opcao = ''
n_elementos = 0
chave = ''
valor = ''

# Impressão do título:
print('.'*79)
print('Dicionário de Ferramentas:')
print('.'*79)

# Escolha do usuário:
print('-'*79)
opcao = str(input('Deseja usar o dicionário pré-definido? (s/n) '))
print('-'*79)

if opcao == 's':
    # Impressão do dicionário pré-definido:
    print('='*79)
    for valor in ferramentas.values():
        print(f'Ferramenta: {valor}')
    n_elementos = len(ferramentas)
    print(f'O dicionário tem {n_elementos} ferramentas.')
    print('='*79)
else:
    ferramentas.clear() # Apaga as ferramentas padrão.
    ferramentas = list(ferramentas) # Faz um casting de ferramentas pata lista.
    print('-'*79)
    
    # Entrada de dados:
    for i in range(1, 6):
        chave = str(input(f'Digite a chave da sua {i}º ferramenta: '))
        valor = str(input(f'Digite o valor da sua {i}º ferramenta: '))
        print('-'*79)
        
        # Processamento de dados:
        ferramenta.clear()
        ferramenta[chave] = valor
        ferramentas.append(ferramenta.copy())
        
    # Saída de dados:
    print('='*79)
    for ferramenta in ferramentas:
        for valor in ferramenta.values():
            print(f'Ferramenta: {valor}')
    n_elementos = len(ferramentas)
    print(f'O dicionário tem {n_elementos} ferramentas.')
    print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)