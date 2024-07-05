# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 04/07/2024.
# J) Faça um programa para criar um dicionário com nomes de frutas.
# Em seguida verifique se tem abacaxi nos valores.

# Importação das bibliotecas:
import os


# Limpeza do terminal:
os.system('cls')

# Declarações de variáveis:
nao_abacaxi = True
dicionario = {}
chute = ''

# Impressão do título:
print('.'*79)
print('Jogo de adivinhação:')
print('Tema: Frutas')
print('.'*79)

# Entrada de dados:
print('(sistema) - "Adivinhe a fruta que estou pensando...')
while nao_abacaxi:
    chute = str(input('Digite o nome de uma fruta: ')).strip().lower()
    
    # Processamento de dados:
    dicionario[chute] = chute
    if 'abacaxi' in dicionario.values():
        nao_abacaxi = False
        break
    else:
        print('Incorreto! Tente outra fruta')
        continue


# Saída de dados:
print('='*79)
print('Parabéns! Você acertou!')
print('Frutas que você chutou: ')
for valor in dicionario:
    print(valor, end = ', ')
print()
print('='*79)

print('.'*79)
print('Fim do jogo! Obrigado por jogar!')
print('.'*79)