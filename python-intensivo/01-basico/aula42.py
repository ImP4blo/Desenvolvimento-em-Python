# Aula 42: Praticando mais com while

frase = 'O Python é uma linguagem de programação ' \
    'Python foi criado por Guido Van Rossum.'

# print(frase.count('Python'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual

    # print(letra_atual, qtd_apareceu_mais_vezes_atual)
    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_que_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x')