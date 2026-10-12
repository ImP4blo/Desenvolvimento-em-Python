# Operadores in e not in
# strings ao iteráveis - Iteraveis é um negocio que vc pode navegar iten por iten - Exemplo: strings, listas, tuplas, dicionários, sets
# 0 1 3 3 4 5
# P a b l o
# -6-5-4-3-2-1

# nome = 'Pablo'
# # print(nome[1]) # a
# # print(nome[-1]) # o

# print('l' in nome) # True
# print('K' in nome) # False
# print('Pab' in nome) # True

# print(10 * '-')
# print('Pab' not in nome) # False
# print('zero' not in nome) # True

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')