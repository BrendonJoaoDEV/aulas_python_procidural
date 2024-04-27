# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 27/04/2024.
# C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade para ajudar a promover a segurança nas estradas.
# Eles precisam de um programa que permita aos usuários inserir a velocidade de um carro e, em seguida, exibir na tela uma mensagem adequada com base na velocidade fornecida.
# O objetivo principal é alertar os motoristas caso ultrapassem o limite de velocidade de 60 km/h, incentivando-os a dirigir dentro dos limites legais e, assim, reduzir o risco de acidentes.

# Importando as bibliotecas.
import os


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*70)
print('Sistema da Safe Drive')
print('Dirija com segurança')
print('.'*70)

# Entrada/Declarações de variáveis.
print('-'*70)
velocidade_carro = str(input('Digite a velocidade do em km/h: '))
velocidade_limite = str('60km/h')
resposta = ''
print('-'*70)

# Processamento
# Condicional para verificar se a velocidade inserida é maior, menor ou igual ao limite.
if velocidade_carro <= velocidade_limite:
    resposta = f'A velocidade de {velocidade_carro} está dentro da velocidade'
    + 'máxima permitida de '
else:
    resposta = f'A veloci'