# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: brendon João Campos Neves.
# Data: 10/06/2024.
# B) Faça um programa que receba o nome 'João da Silva' e,
# em seguida, substitua 'Silva' por 'Oliveira'.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo o título.
print('.'*79)
print('SUNSTITUINDO O SOBRENOME')
print('.'*79)

# Entrada de dados.
print('-'*79)
nome =  'João da Silva'
print('Digite seu nome: João da Silva')
print('-'*79)

# Processamento de dados.
novo_nome = nome.replace('Silva', 'Oliveira')

# Saída de dados.
print('='*79)
print(f'Seu nome é {nome}')
print(f'Após a substituição ficou: {novo_nome}')
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)