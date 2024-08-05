# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 11/07/2024.
# Autor: Brendon João Campos Neves.
# A) Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares,
# a quantidade de números pares e a quantidade de números ímpares.

# Definindo funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def pares_impares(lista_numeros):
    pares = []
    impares = []
    for i in lista_numeros:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

        # Processo que remove elemento duplicados das listas:
        pares = set(pares)
        impares = set(impares)
        pares = list(pares)
        impares = list(impares)

    return pares, len(pares), impares, len(impares)


# Declarações de variáveis:
numero = ''
numeros = []
opcao = ''

# Limpando o terminal:
limpar_terminal()

print('.'*79)
print('Separando números pares e ímpares:')
print('.'*79)

# Entrada de dados que pergunta ao usuário se deseja adicionar outro elemento:
print('-'*79)
while True:
    numero = input('Digite os números que deseja verificar, um por um: ')
    if numero.isnumeric():
        numeros.append(int(numero))
        opcao = str(input('Deseja adicionar outro número? (s/n) ')
                    ).strip().lower()
        if opcao == 's':
            continue
        else:
            print('-'*79)
            numeros = set(numeros)
            numeros = list(numeros)
            break
    else:
        print('Entrada inválida! Digite apenas números inteiros!')

# Invocação da função com umpacking:
pares, n_pares, impares, n_impares = pares_impares(numeros)

# Ordenando listas:
numeros.sort()
pares.sort()
impares.sort()

# Saída dos resultados:
print('='*79)
print('Lista analisada:')
for numero in numeros:
    print(numero, end=', ')
print()
print('Números pares:')
for n_par in pares:
    print(n_par, end=', ')
print()
print('Números ímpares:')
for n_impar in impares:
    print(n_impar, end=', ')
print()
print('Na sua lista de números existem:')
print(f'{n_pares} números pares.')
print(f'{n_impares} números ímpares.')
print('='*79)

# Aviso de fim
print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
