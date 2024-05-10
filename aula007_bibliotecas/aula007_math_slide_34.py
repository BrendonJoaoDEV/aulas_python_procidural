# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João CAmpos Neves.
# Data: 09/05/2024.
# Biblioteca math: potencia, raiz quadrada, hipotenusa e calculadora trigonométrica.

# Importando as bibliotecas.
import os
import math


# Limpando o terminal.
os. system('cls')

print('-'*70)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')
print('='*70)
print()

# Declarações.
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5 # cateto oposto.
ca = 10 # cateto adjacente.

# Processamento.
potencia = math.pow(base, expoente)
raizQuadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

# Saída.
print(f'{base} elevado a {expoente} é igual a: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizQuadrada}')
print(f'O seno de {angulo} é: {seno: .2f}')
print(f'O cosseno de {angulo} é: {cosseno: .2f}')
print(f'A tangente de {angulo} é: {tangente: .2f}')
print(f'O valor da hipotenusa é: {hipotenusa: .2f}')
print('-'*70)