# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 17/04/2024.
# Exercícios f-strings e variáveis.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system("cls")

print("-" * 70)
print("ENTRADA DE DADOS")
print("=" * 70)

# Entrada em Casting.
produto = str(input("Entre com o produto: "))
preco = float(input("Entre com o preço do produto: "))
parcelamento_maximo = int(input("Entre com o limite de parcelas: "))
possui_estoque = bool(True)

# Saída Interpolada.
print("-" * 70)
print("SAÍDA DE DADOS")
print("=" * 70)
print(f"O {produto}")
print(f"Está {possui_estoque} no estoque")
print(f"Seu preço é de {preco}")
print(f"Esse valor pode ser parcelado em até {parcelamento_maximo} vezes")

# Tipo das variáveis.
print("-" * 70)
print("TIPO DAS VARIÁVEIS")
print("=" * 70)
print("A variável produto é do", type(produto))
print("A variável preço é do", type(preco))
print("A variável parcelamento máximo é do", type(parcelamento_maximo))
print("A variável possui estoque é do", type(possui_estoque))
print("-" * 70)
print("")
