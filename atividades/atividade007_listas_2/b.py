# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 16/06/2024.
# B) Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

# Importando as bibliotecas do sistema:
import os


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
entrada = ''
notas_lidas = 0
notas = []
notas_inversa = []
quantidade_notas = 0
soma = 0 + 0
media = soma / 1

# Imprimindo o título:
print('.'*79)
print('ARMAZENANDO E PROCESSANDO NOTAS DE ALUNOS')
print('PRESSIONE "s" OU "0" PARA SAIR')
print('.'*79)

# Entrada de dados:
while True:
    entrada = input('Digite a nota do aluno: ')
    if ((entrada == 's') or (entrada == '0')):
        break
    else:
        notas.append(int(entrada))
        continue

# Processamento de dados:
# Número de notas lidas:
notas_lidas = len(notas)

# Soma das notas:
for nota in notas:
    soma += nota

# Média das notas:
media = soma / len(notas)

# Notas inversas:
notas_inversa = notas.copy()
notas_inversa.reverse()

# Saída de dados:
print('='*79)
print(f'Número de notas lidas: {notas_lidas}')
print(f'Lista de notas dos alunos: {notas}')
print('Lista de notas dos alunos em ordem inversa: ')
for nota in notas_inversa:
    print(nota)
print(f'A soma das notas de todas os alunos é {soma}')
print(f'A média das notas de todos os alunos é {media}')
print('='*79)

# Imprimindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)