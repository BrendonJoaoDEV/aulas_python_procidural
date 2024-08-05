# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 05/08/2024.
# Autor: Brendon João Campos Neves.
# I) Faça um programa de perguntas e respostas sobre os estados
# e capitais brasileiras. O programa deverá exibir para o usuário
# o estado e perguntar qual a sua capital. Se o usuário errar a resposta,
# o programa será finalizado apresentando quantas perguntas estão corretas.
# Utilize ao menos uma função e não há a necessidade de modularizar o código.

# Definindo funções:
def limpar_terminal():
    import os
    import platform

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def pergunta_aleatoria():
    estado = random.choice(list(estados_capitais.keys()))
    print(f'Qual a capital do estado {estado}?')


# Importação de bibliotecas:
import random


# Declarações de variáveis:
estados_capitais = {
    'Acre (AC)' : 'Rio Branco',
    'Alagoas (AL)' : 'Maceió',
    'Amapá (AP)' : 'Macapá',
    'Amazonas (AM)' : 'Manaus',
    'Bahia (BA)' : 'Salvador',
    'Ceará (CE)' : 'Fortaleza',
    'Distrito Federal (DF)' : 'Brasília',
    'Espírito Santo (ES)' : 'Vitória',
    'Goiás (GO)' : 'Goiânia',
    'Maranhão (MA)' : 'São Luís',
    'Mato Grosso (MT)' : 'Cuiabá',
    'Mato Grosso do Sul (MS)' : 'Campo Grande',
    'Minas Gerais (MG)' : 'Belo Horizonte',
    'Pará (PA)' : 'Belém',
    'Paraíba (PB)' : 'João Pessoa',
    'Paraná (PR)' : 'Curitiba',
    'Pernambuco (PE)' : 'Recife',
    'Piauí (PI)' : 'Teresina',
    'Rio de Janeiro (RJ)' : 'Rio de Janeiro',
    'Rio Grande do Norte (RN)' : 'Natal',
    'Rio Grande do Sul (RS)' : 'Porto Alegre',
    'Rondônia (RO)' : 'Porto Velho',
    'Roraima (RR)' : 'Boa Vista',
    'Santa Catarina (SC)' : 'Florianópolis',
    'São Paulo (SP)' : 'São Paulo',
    'Sergipe (SE)' : 'Aracaju',
    'Tocantins (TO)' : 'Palmas'
}
estado = ''
resposta = ''
numero_acertos = 0

limpar_terminal()

print('.'*79)
print('Quiz: Estados Brasileiros')
print('.'*79)

print('-'*79)
while True:
    pergunta_aleatoria()
    resposta = input(str('Digite o nome da capital: '))
    print('-'*79)
    if (resposta != estados_capitais[estado]):
        break
    else:
        numero_acertos += 1
        continue

print('='*79)
print('Você errou... Que pena...')
print(f'Você acertou {numero_acertos} perguntas, parabéns!')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)