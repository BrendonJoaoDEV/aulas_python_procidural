# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 04/06/2024.
# L) Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('SISTEMA DE LOGIN')
print('.'*79)

# Declarações de vriáveis.
usuario = ''
senha = ''
usuario_base = ''
senha_base = ''
confirmacao = ''

# Entrada de dados.
# Definindo a senha.
print('.'*79)
print('DEFINA SEU USUÁRIO E SENHA')
print('.'*79)
while True:
    print('-'*79)
    usuario_base = input('Digite seu nome de usuário: ')
    senha_base = input('Digite sua senha: ')
    confirmacao = input('Confirme sua senha: ')
    print('-'*79)
    # Validação da senha.
    if (senha_base == confirmacao):
        break
    else:
        print('Sua senha e a confirmação são diferentes.')

# Processamento de dados.
print('.'*79)
print('FAÇA SEU LOGIN')
print('.'*79)
while True:
    print('-'*79)
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    print('-'*79)
    # Verificação do usuário e senha.
    if ((usuario == usuario_base) and (senha == senha_base)):
        # Saída de dados.
        print('='*79)
        print(f'Seja bem vindo {usuario_base}!')
        print('='*79)
        break
    else:
        print('Senha ou usuário inválidos!')

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)