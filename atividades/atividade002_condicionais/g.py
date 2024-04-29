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

# Processamento.
# Condicional:
# if(verifica se os segmentos respeitam a desigualdade triângular).
# else(caso os segmentos não respeitem a desigualdade triângular).
if (segmento_1 + segmento_2 > segmento_3 and
+ segmento_1 + segmento_3 > segmento_2 and
+ segmento_2 + segmento_3 > segmento_1):
    resposta = (f'Os segmentos {segmento_1}, {segmento_2} e '
+ f'{segmento_3} podem formar um triângulo!')
else:
    resposta = (f'Os segmentos {segmento_1}, {segmento_2} e '
+ f'{segmento_3} não podem formar um triângulo!')

# Saída
print('='*70)
print(resposta)
print('='*70)

# Título de fim.
print('.'*70)
print('Fim do programa!')
print('.'*70)
print()