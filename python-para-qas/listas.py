

lista_de_compras = ['Leite', 'Nescal', 'Pão', 'Requeijão', 'Café']

numeros_da_sorte = [2, 4, 12, 44, 77, 71]

# print(lista_de_compras)
# print(numeros_da_sorte)

#O Jeito abaixo é uma forma de imprimir linha a linha, mas não é umm jeito interessante de se fazer, pois não é escalável. Se a lista tiver 100 itens, você terá que escrever 100 linhas de código para imprimir cada item.
# print(lista_de_compras[1])  # Acessando o segundo item da lista (índice 1)
# print(lista_de_compras[2])
# print(lista_de_compras[3])
# print(lista_de_compras[4]) 


#Abaixo é um jeito melhor e escalável de imprimir todos os itens da lista, usando um loop `for`. Assim, não importa quantos itens a lista tenha, o código continuará funcionando corretamente.
for produto in lista_de_compras:
    print(produto)

