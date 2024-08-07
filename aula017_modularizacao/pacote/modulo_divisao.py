# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 06/08/2024.

def dividir(a, b):

    """Método para dividir 2 números

    Args:
        a (any): Dividendo
        b (any): Divisor
    
    Returns:
        Str: Mensagem de erro ou 'Ok!' se a divisão for bem-sucedida
        Any: Quociente ou None em caso de erro
    """

    if b == 0:
        return None, 'Erro de divisão'
    else:
        divisao = a / b
        return divisao, 'Ok!'