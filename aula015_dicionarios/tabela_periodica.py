# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 27/06/2024.
# Tabela periódica com: adição, visualização, atualização e remoção de elementos.

import os


os.system('cls')

print('-'*70)
print('---------- TABELA PERIÓDICA -----')
print('='*70)

# Inicialização do dicionário e da lista.
elementos = {}  # Dicionário.
periodica = []  # Lista.

while True:
    os.system('cls')

    # Cabeçalho do menu.
    print('-'*70)
    print('MENU DE OPÇÕES:')
    print('='*70)
    print('1. Adicionar um elemento')
    print('2. Visualizar todos os elementos')
    print('3. Atualizar um elemento')
    print('4. Remover um elemento')
    print('5. Sair')
    print('-'*70)

    # Solicitação da escolha do usuário.
    opcao = input('Escolha uma opção (1-5): ')

    if opcao == '1':
        # Adicionar um elemento.
        simbolo = str(input('Símbolo do elemento: '))
        nome = str(input('Nome do elemento: '))
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())
        input('\nElemento adicionado. Pressione Enter para continuar...')

    elif opcao == '2':
        # Visualizar todos os elementos.
        print('\nElementos na tabela periódica:')
        print('-'*70)
        for elemento in periodica:
            for chave, valor in elementos.items():
                print(f'{chave.capitalize()} : {valor}')
            print('-'*70)
        input('\nPressione Enter para continuar...')

    elif opcao == '3':
        # Atualizar um elemento.
        simbolo = str(input('Digite o símbulo do elemento para atualizar: '))
        # Inicializa a flag como False.
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input('Digite o novo símbolo para'
                                        f' {simbolo} (ou deixe em branco para manter o atual): '))
                novo_nome = str(input('Digite o novo nome para'
                                        f' {simbolo} (ou deixe em branco para manter o atual): '))

                # Atualiza o símbolo e o nome se fornecidos.
                if novo_simbolo:
                        elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome
                # Define a flag como  True quando o elemento é encntrado.
                encontrado = True
                break

        if encontrado:
            input('\nElemento atualizado. Enter oara continuar...')
        else:
            input('\nElemento não encontrado. Enter para continuar...')

    elif opcao == '4':
        # Remover um elemento.
        simbolo = str(
            input('Digite o símbolo do elemento que deseja remover: '))
        encontrado = False # Inicializa a flag como False.
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                periodica.remove(elemento)
                # Define a flag como True quando o elemento é encontrado.
                encontrado = True
                break
        if encontrado:
            input('\nElemento removido. ENter para continuar...')
        else:
            input('\nElemento ')
