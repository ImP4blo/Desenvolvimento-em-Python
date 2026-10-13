# Aula 27: Fatiamento de strings e len()
"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs: a função len retorna a qtd de caracteres da string
"""

variavel = 'Ola mundo'
print(variavel[4])  # Retorna a letra na posição 4 - no caso, a letra 'm'
print(variavel[-4])  # Retorna a letra na posição -4 - No caso, a letra 'u'
print(variavel[4:]) # Retorna a string a partir da posição 4 - no caso, 'mundo'
print(variavel[4:7]) # Retorna a string da posição 4 até a posição 7 - no caso, 'mun'
print(len(variavel)) # Retorna a quantidade de caracteres da string - no caso, 9
print(len(variavel[4])) # Retorna extamente a quantidade de caracteres da string na posição 4 - no caso, 1
print(variavel[0:9:2]) # Retorna a string da posição 0 até a posição 9, pulando de 2 em 2 - no caso, 'Oamno'
print(variavel[::-1]) # Retorna a string de trás para frente - no caso, 'odnum alO'