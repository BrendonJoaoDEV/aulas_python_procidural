# Curso de Desenvolvimento de Sistemas
# Turma:0152
# Autor: Brendon joão Campos Neves
# Data: 15/04/2024
# Variáveis

# Importando as bibliotecas de sistema
import os


# Limpando o terminal
os.system( "cls" )

print ( "_" * 70 ) # Firula
print ( "Estudo de variaveis" )
print ( "_" * 70 )

# As variáveis são declaradas porinferência
nome = "John Doe"
nascimento = 1970
peso = 75.5
doador = True
complexo = 3J # Python trabalha diretamente com números complexos
PI = 3.14 # Isso é uma CONSTANTE, seu valor não deve ser alterado

# Saída utilizando o método type() para verificar o tipo da variável
print ( "\033 [0m \033 [31mTipos declarados:\033 [0m" )
print ( "\033 [0m A var \033 [32m nome \033 [0m é do tipo: " , type ( nome ) )
print ( "\033 [0m A var \033 [32m nascimento \033 [0m é do tipo: " , type ( nascimento ) )