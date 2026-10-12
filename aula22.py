# Operadores Lógicos
# and (e) or (ou) not (não)
# And - Todas as condições precisam ser verdadeiras para que o resultado seja verdadeiro.
# Se quaqulquer condição for falsa, a expressao inteira sera avaliada naquele valor falso.
# São considerados falsy (que nos ja vimos)
# 0 0.0 '' False
# Tambem existe tipo None que é usado para reprentar um nao valor

#avaliacao de curto circuito
# exemplol: print(true and False and True) # False - Retorna false pois a primeira condicao ja e falsa, entao nao precisa avaliar as outras
# print(bool('')) - Flase - Esse e um exemplo de curto circuito, pois a primeira condicao ja e falsa, entao nao precisa avaliar as outras

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '1234567'

# #if True:
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')

# else:
#     print('Sair')


#avaliacao de curto circuito
# senha = 0 or False or 0 or '' or 'abc' or True
# print(senha) # abc - Retorna abc pois e o primeiro valor verdadeiro encontrado, entao nao precisa avaliar as outras

senha = input('Senha: ') or 'Sem senha'
print(senha) # Sem senha - Retorna Sem senha pois o input e vazio, entao nao precisa avaliar as outras