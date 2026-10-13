# Aula 32 (exercícios): Par ou ímpar, saudação por horário e tamanho do nome
"""
Faça um programa que pergunte ao usuário para digitar um número inteiro,
informe se ese número é par ou impar. Caso o usuário nao digite um nuumero inteiro, informe
que não é um numero inteiro.
"""

# numero_inteiro = int(input('Digite um número inteiro: '))

# numero_impar = numero_inteiro % 2 > 0

# try:
#     numero_inteiro = int(input('Digite um número inteiro: '))
# except ValueError:
#     print('Voce não digitou um numero inteiro')

# else:
#     numero_par = numero_inteiro % 2 == 0

#     if numero_par:
#         print('Voce digitou um número par')
#     else:
#         print('Voce digitou um número impar')






"""
Faça um programa que pergunte a hora ao usuário e, baseando se no horário descrito, exiba 
Saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# try:
#     hora_atual = int(input('Digite que horas são agora: '))
# except ValueError:
#     print('Voce não digitou um numero válido')

# else:

#     if hora_atual >= 0 and hora_atual <= 11:
#         print('Bom dia')

#     if hora_atual >= 12 and hora_atual <= 17:
#         print('Boa tarde')

#     if hora_atual >= 18 and hora_atual <= 23:
#         print('Boa noite')

#     if hora_atual >= 24:
#         print('Vc nao digitou um número válido. Digite de zero a 23')

#     if hora_atual <= -1:
#         print('Vc digitou número negativo, coloque um número não negativo de 0 a 23')


#Como o Professor fez:

# entrada = input('Digite a hora em númeiros inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#         print('Nao conehço esse horário. Digite um número de 0 a 23')
# except:
#     print('Você não digitou um número inteiro válido. Tente novamente.')


"""
Faça um programa que peça ao primeiro nome do usuário. Se o nome tiver 4 letras ou menos
Escreva "Seu nome é curto", Se tiver entre 5 e 6 letras, escreva
"seu nome é normal", maior que 6 escreva "Seu nome é muito grande".
"""

# primeiro_nome = input('Digite seu Primeiro nome: ')

# try:
#    float(primeiro_nome)
# except ValueError:
#     if len(primeiro_nome) <= 4:
#         print('Seu nome é curto')
#     if len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
#         print('Seu nome é normal')
#     if len(primeiro_nome) > 6:
#         print('Seu nome é muito Grande')
# else:
#     print('Voce digitou um numero. Digite letras')


# como o Professor fez:

# nome = input('Digite seu primeiro nome: ')
# tamanho_nome = len(nome)

# if tamanho_nome >= 1:
#     if tamanho_nome <= 4:
#         print('Seu nome é curto')
#     elif tamanho_nome >= 5 and tamanho_nome <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# else:
#     print('Por favor, Digite pelo menos uma letra.')
