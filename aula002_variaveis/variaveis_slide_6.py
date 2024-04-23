# Curso de Desenvolvimento de Sistemas.
# Turma:0152.
# Autor: Brendon joão Campos Neves.
# Data: 15/04/2024.
# Variáveis.

# Importando as bibliotecas.
import os


# Limpando o terminal.
os.system("cls")

# Firula.
print("_" * 70)
print("Estudo de variaveis")
print("_" * 70)

# As variáveis são declaradas porinferência.
nome = "John Doe"
nascimento = 1970
altura = 1.80
peso = 75.5
doador = True
# Python trabalha diretamente com números complexos.
complexo = 3J
# Isso é uma CONSTANTE, seu valor não deve ser alterado.
PI = 3.14

# Saída utilizando o método type() para verificar o tipo da variável.
print("\033 [0m \033 [31m Tipos declarados: \033 [0m")
print("\033 [0m A var \033 [32m nome \033 [0m é do tipo: ", type(nome))
print("\033 [0m A var \033 [32m nascimento \033 [0m é do tipo: ", type(nascimento))
print("\033 [0m A var \033 [32m altura \033 [0m é do tipo: ]", type(altura))
print("\033 [0m A var \033 [32m peso \033 [0m é do tipo: ", type(peso))
print("\033 [0m A var \033 [32m doador \033 [0m é do tipo: ", type(doador))
print("\033 [0m A var \033 [32m complexo \033 [0m é do tipo: ", type(complexo))
print("\033 [0m A var \033 [32m PI \033 [0m é do tipo: ", type(PI))
print("_"*70)
print("")
