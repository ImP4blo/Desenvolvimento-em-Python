# Conversao de tipo, coerção
# Type convertion, typecasting, coercion
# é o ato de converter um tipo de dado em outro tipo de dado.
# tipos imutaveis e primitivos:
# str, int, float, bool

# print(1 + 1 )
print(int('1'), type(int('1')) ) # converte string para inteiro

print(int('1') + 1) # soma inteiro com inteiro
print(type(float('1.2') + 1)) # converte string para float e soma
print(bool('')) # converte string vazia para booleano
print(str(44) + 'p') # converte inteiro para string e concatena