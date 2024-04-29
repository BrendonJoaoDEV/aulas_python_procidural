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
salario_atual = float(input('Digite o valor de seu salário atual: R$'))
reajuste = ''
salario_reajustado = ''
resposta = ''
print('-'*70)

# Processamento.
# Condicional: 
# if(verificar se o valor do saĺario é positivo maior que zero).
# 1ºelif(verificar se o salário é superior a R$1500.00).
# 2ºelif(verificar se o salário é inferior a R$100.00).
# else(caso contrário o salário não é alterado).
if salario_atual <= 0:
    resposta = 'O valor de salário informado é inválido'
    'por favor digite um valor diferente de 0 e positivo'
elif salario_atual > 1500.00:
    reajuste = salario_atual * 5/100
    salario_reajustado = salario_atual + reajuste
    resposta = (f'Seu salário no valor de R${salario_atual} '
    + f'foi reajustado em +R${reajuste} '
    + f'passando a ser R${salario_reajustado}')
elif salario_atual < 1000.00:
    reajuste = salario_atual * 10/100
    salario_reajustado = salario_atual + reajuste
    resposta = (f'Seu salário no valor de R${salario_atual} '
    + f'foi reajustado em +R${reajuste} '
    + f'passando a ser R${salario_reajustado}')
else:
    resposta = ('Seu salário está entre R$1000.00 e R$1500.00 0'
    'por isso não sofreu nenhum reajuste')

# Saída.
print('='*70)
print(resposta)
print('='*70)

print('.'*70)
print('Fim do programa!')
print('.'*70)