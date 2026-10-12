"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'pablo  Mateus'
outra_variavel = f'{string[:4]}007{string[6:]}'
# string[4] = '007' # vai dar erro, pois strings são imutáveis
print(outra_variavel)
print(string.capitalize())