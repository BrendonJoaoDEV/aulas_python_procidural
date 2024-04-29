# Curso de Desenvolvimento de Sistemas.
# Turma; 0152.
# Autor: Brendon João Campos Neves.
# Data: 28/04/2024.
# E) A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de passagens de ônibus com base na distância da viagem.
# Eles precisam de um programa que solicite ao usuário a distância a desejada e, em seguida, calcule o preço da passagem de acordo com as políticas da empresa.
# Segundo essas políticas, viagens de até 200 km têm um custo de R$0,70 por km rodado, enquanto viagens acima dessa distância passam a custar R$0,40 por km rodado.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*70)
print('Sistema da Travel Calc')
print('Calcular valor da passagem')
print('.'*70)

# Entrada/Declaração de variáveis.
print('-'*70)
distancia = float(input('Digite quantos km deseja viajar: '))
valor_da_viagem = ''
resposta = ''
print('-'*70)

# Processamento.
# Condicional:
# if(verifica se a viagem tem até 200 km).
# else(calcula viagens com mais de 200 km).
if distancia <= 200:
    valor_da_viagem = distancia * 0.70
    resposta = f'Sua viagem de {distancia}km ira custar {valor_da_viagem}'
else:
    valor_da_viagem = distancia * 0.40
    resposta = f'Sua viagem de {distancia}km ira custar {valor_da_viagem}'

# Saída.
print('='*70)
print(resposta)
print('='*70)

print('.'*70)
print('Fim do programa!')
print('.'*70)