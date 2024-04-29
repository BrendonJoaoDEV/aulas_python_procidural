# Curso de Desenvolvimento de Sistemas - SENAC.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 29/04/2024.
# H) A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de equações quadráticas para auxiliar engenheiros e cientistas em suas análises e projetos.
# Eles precisam de um programa que calcule as raízes da equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos, utilizando apenas os conceitos e operações básicas aprendidos até o momento.
# Essas raízes são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser capaz de calcular essas raízes de forma precisa, seguindo os princípios matemáticos fundamentais.

# Impotando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*70)
print('Sistema da Root Calc')
print('Calcular raízes de equações quadráticas')
print('.'*70)

# Entrada de dados/Declaração de variáveis.
print('-'*70)
a = 1
b = -6
c = 5
delta = b**2 - 4*a*c
bhaskara_mais = (-b + delta**0.5) / 2*a
bhaskara_menos = (-b - delta**0.5) /2*a
x_mais = ''
x_menos = ''
print('Dada a equação 𝑥²−6𝑥+5')
print('-'*70)

# Processamento.
# Condicional:
if delta > 0:
    x_mais = f'A raiz + de 𝑥²−6𝑥+5 é {bhaskara_mais}'
    x_menos = f'A raiz - de 𝑥²−6𝑥+5 é {bhaskara_menos}'
else:
    resposta = (f'Essa equação não pode ser realizada porque '
                + f'delta não pode ser negativo ou zero')

# Saída.
print('='*70)
print(x_mais)
print(x_menos)
print('='*70)

# Título de fim.
print('.'*70)
print('Fim do programa!')
print('.'*70)
print()