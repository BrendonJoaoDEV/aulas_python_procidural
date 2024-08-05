# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 05/08/2024.
# Autor: Brendon João Campos Neves.
# G) Crie um programa que peça ao usuário 2 números maiores que 0
# e menores que 11.
# Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto
# : 4. Divisão : 4. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior
# ou  igual a 1 e menor ou igual a 6.
# Em seguida, você criará funções que retornem os resultados das operações,
# imprimindo os resultados na tela.

# Definindo funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def somar(a, b):
    soma = a + b
    return soma


def subtrair(a, b):
    subtracao = a - b
    return subtracao


def multiplicar(a, b):
    multiplicacao = a * b
    return multiplicacao


def dividir(a, b):
    divisao = a / b
    return divisao


def dividir_inteiramente(a, b):
    divisao_inteira = a // b
    return divisao_inteira


def resto_divisao(a, b):
    resto = a % b
    return resto


# Declarações de variáveis:
a = 0
b = 0
resultado = 0

limpar_terminal()

print('.'*79)
print('Calculadora')
print('.'*79)

# Entrada de dados:
print('-'*79)
while True:
    a = input('Digite um número entre 0 e 11: ')
    b = input('Digite outro número entre 0 e 11: ')
    if (a.isnumeric() and b.isnumeric()):
        a = int(a)
        b = int(b)
        if (a >= 0 and a <= 11):
            if (b >= 0 and b <= 11):
                break
            else:
                print('Seu 2º valor não está entre 0 e 11!')
                continue
        else:
            print('Seu 1º valor '
                  'não está entre 0 e 11!')
            continue
    else:
        print('Digite apenas números '
              'inteiros entre 0 e 11!')
        continue
print('-'*79)
while True:
    print('Escolha a operação que deseja'
          'realizar com seus valores')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Divisão inteira')
    print('6 - Resto da divisão')
    
    opcao = input('Digite o número da opção desejada: ')
    
    # Processamento de dados:
    if (opcao == '1'):
        resultado = somar(a, b)
        break
    elif (opcao == '2'):
        resultado = subtrair(a, b)
        break
    elif (opcao == '3'):
        resultado = multiplicar(a, b)
        break
    elif (opcao == '4'):
        resultado = dividir(a, b)
        break
    elif (opcao == '5'):
        resultado = dividir_inteiramente(a, b)
        break
    elif (opcao == '6'):
        resultado = resto_divisao(a, b)
        break
    else:
        print('Opcão inválida!')
        continue

# Saída de dados:
print('='*79)
print(resultado)
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)