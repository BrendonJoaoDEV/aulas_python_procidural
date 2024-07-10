# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 09/07/2024.

# definindo funções:

def limpa_tela():
    """Função para limpar o terminal
    """
    import os
    os.system('cls')


def soma(a, b):
    """Função para somar 2 números

    Args:
        a (int): Valor de a
        b (int): Valor de b

    Returns:
        Retorna a soma de 2 números
    """
    return a + b


def firula():
    print('-'*70)

# Programa principal:


# Chamando as funções:
limpa_tela()
firula()
resposta = soma(1, 2)
print(f'A soma dos 2 números é: {resposta}')
firula()
print()