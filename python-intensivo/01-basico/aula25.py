# Aula 25: Interpolação de strings com %
"""
Interpolação básica de strings

s - strings
d e i - int
f - float
x e x -Hexadecimal (ABCDEF0123456789)
# > - esquerda
"""


nome = 'Pablo'
preco = 1000.958976
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (15, 15))