# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Brendon João Campos Neves.
# Data: 10/07/2024.
# Desafio: Calcular a velocidade média em km/h e min/m.

import os


os.system('cls')

# Declarações de variáveis:
distancia = 0.0
tempo = 0.0
unidade = ''
velocidade_media = 0
resultado = ''

# Definindo uma função:
def calcular_velocidade_media(distancia, tempo):
    # Vm = Δs/Δt
    velocidade_media = distancia / tempo
    return velocidade_media

distancia = float(input('Digite a distância percorrida (em km ou metro): '))
tempo = float(input('Digite o tempo gasto (em horas ou minutos): '))
unidade = str(input('Suas unidades são km/h ou m/min? ')).strip().lower()
velocidade_media = calcular_velocidade_media(distancia, tempo)
resultado = f'A velocidade media é {velocidade_media: .2f} {unidade}'
print(resultado)