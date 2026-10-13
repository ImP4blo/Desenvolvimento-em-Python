# Aula 28: Exercício: analisando o nome do usuário
"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:

    Exiba:
         seu nome é {nome}
         Seu nome invertido é {nome invertido}
         Seu nome contém (ou não) espaços
         Seu nome tem {n} letras
         A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
        "Desculpe, você não digitou nada."
"""

nome = input('Digite seu nome ')
idade = input('Digite sua idade ')

if nome and idade:
    print('Seu nome é:',nome)
    print('seu nome invertido é:',(nome[::-1]))
    print('Seu nome contém espaços:', ' ' in nome) 
    print(f'Seu nome tem {len(nome.replace(' ', ''))} letras')
    print('A primeira letra do seu nome é:',nome[0])
    print('A última letra do seu nome é:', nome[-1])

else:
    print('Desculpe, você deivou campos vazios')

# if ' ' in nome:
#     print('Seu nome contém espaços')
# else:
#     print('Seu nome nao contem espaços')
