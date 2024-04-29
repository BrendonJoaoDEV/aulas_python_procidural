# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 28/04/2024.
# D) A empresa "SalaryBoost" está implementando um sistema automatizado para calcular os aumentos salariais de seus funcionários com base em critérios específicos.
# Eles precisam de um programa que receba como entrada o salário atual de um funcionário e, em seguida, calcule o novo salário com base em determinadas condições.
# Essas condições incluem um aumento de 5% caso o salário atual seja superior a R$1500,00, e um aumento de 10% caso o salário atual seja inferior a R$1000,00.
# Além disso, o programa deve garantir que o salário informado não seja igual a zero ou negativo, pois isso não seria válido.

# Importando as bibliotecas.
import os


# Limpando o terminal.
os.system('cls')


# Título.
print('.'*70)
print('Sistema da Salary Boost')
print('Aumento salarial')
print('.'*70)

# Entrada/Declaração de variáveis.
print('-'*70)
salario_atual = 