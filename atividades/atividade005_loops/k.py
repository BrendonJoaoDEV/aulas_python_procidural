# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 04/06/2024.
# K) Crie um programa que pede que o usuário digite um nome ou uma frase,
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('É UM PALÍNDROMO?')
print('.'*79)

# Declarações de variáveis.
frase = ''
sem_espaço = ''
invertida = ''
resposta = ''

# Entarda de dados.
while True:
    print('-'*79)
    frase = input('Digite a frase que deseja verificar: ')
    print('-'*79)
    # Validação de dados.
    if (frase.isnumeric()):
        print('Entrada inválida!')
    else:
        break

# Processameento de dados.
sem_espaço = frase.replace(' ', '').lower()
invertida = sem_espaço[::-1]
if (sem_espaço == invertida):
    resposta = f'{frase} é um palíndromo!'
else:
    resposta = f'{frase} não é um palíndromo!'

# Saída de dados.
print('='*79)
print(resposta)
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)