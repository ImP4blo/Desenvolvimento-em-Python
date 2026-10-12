# O porteiro Eletronico

print("Bem-vindo ao Porteiro Eletrônico")

# passo 1 - Entrada de dados

idade_texto = input('Qual é a sua idade? ')

idade = int(idade_texto)

#2 logica de verificação - Orde: Idoso -> Adulto -> Menor

if idade >= 60:
    print('Voce tem entrada grátis! Aproveite!')

elif idade >= 18:
    print('Sua entrada é R$ 20,00. Bem-vindo!')

else:
    print('Acesso permitido somente parea maiores de 18 anos. Volte quando tiver idade suficiente!')


# Exemplo rápido mostrando várias condições com `elif`
print("\n--- Exemplo rápido de várias condições ---")
num = int(input('Digite um número inteiro (exemplo): '))
if num < 0:
    print('Número negativo')
elif num == 0:
    print('Zero')
elif num <= 10:
    print('Entre 1 e 10')
else:
    print('Maior que 10')


# Exercício: classificar uma nota usando if / elif / else
# print("\n--- Exercício: Classificar nota ---")
# print('Descrição: escreva um bloco if/elif/else que converta uma nota (0-100) em conceito:')
# print('>=90: A, 80-89: B, 70-79: C, 60-69: D, <60: F')
# input('Tente primeiro no seu editor. Pressione Enter para ver uma solução de exemplo...')

# def mostrar_solucao_nota():
#     nota_text = input('Digite uma nota (0-100) para ver a solução de exemplo: ')
#     try:
#         nota = int(nota_text)
#     except ValueError:
#         print('Entrada inválida. Use um número inteiro entre 0 e 100.')
#         return

#     if nota >= 90:
#         print('Conceito: A')
#     elif nota >= 80:
#         print('Conceito: B')
#     elif nota >= 70:
#         print('Conceito: C')
#     elif nota >= 60:
#         print('Conceito: D')
#     else:
#         print('Conceito: F')

# mostrar_solucao_nota()