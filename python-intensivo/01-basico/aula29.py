"""
Introdução ao try/except
try -> Tenta executar um bloco de código e, caso ocorra algum erro, o programa não é interrompido, e sim tratado pelo except.
except -> Bloco de código que é executado caso ocorra algum erro no bloco try.
"""

# print(1234)
# print(567)
# int(a) # Erro de execução, pois a variável 'a' não foi definida. O programa será interrompido.

# numero_str = input('Vou dobrar o número que você digitar: ')

# print(numero_str.isdigit()) # Verifica se o valor digitado é um número inteiro positivo.


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Você não digitou um número válido. Tente novamente.')

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('Você não digitou um número válido. Tente novamente.')