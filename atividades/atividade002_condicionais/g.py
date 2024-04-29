# Curso de Desenvolvimento de Sistemas - SENAC.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 29/04/2024.
# G) Você está desenvolvendo um programa para determinar se três segmentos podem formar um triângulo.
# Para isso, o programa precisa receber as medidas dos três segmentos e compará-las entre si.
# A resposta resultante dessa comparação deve indicar se os segmentos fornecidos podem formar um triângulo ou não.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Título
print('.'*70)
print('Sistema da Geometric Calculations')
print('Verificar se os segmentos podem ser um triângulo')
print('.'*70)

# Entrada de dados/Declaração de variáveis.
print('-'*70)
segmento_1 = float(input('Digite o valor do 1º segmento: '))
segmento_2 = float(input('Digite o valor do 2º segmento: '))
segmento_3 = float(input('Digite o valor do 3º segmento: '))
resposta = ''
print('-'*70)