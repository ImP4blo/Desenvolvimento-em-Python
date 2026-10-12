
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo nao tem fim
"""

contador = 0

while contador <= 100:
    contador += 1


    if contador == 6:
        print('Não vou exibir o 6')
        continue

    if contador >= 20 and contador <= 30:
          
            continue

    print(contador)

    if contador == 44:
        break


 
print('Acabou')



