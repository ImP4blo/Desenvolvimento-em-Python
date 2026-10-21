# Aula 43: Aprendendo FOR 

# texto = 'Python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)

#     i += 1


# senha_salva = '1234567'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(f'O numero de repetições foi: {repeticoes}')
# print('Aquele laço acima pode ter repeticoes infinitas')



# for letra in 'Python':
#     if letra == 'z':
#         print('Achei o h!')
#         break
# else:
#     print('Não tem z')


texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)