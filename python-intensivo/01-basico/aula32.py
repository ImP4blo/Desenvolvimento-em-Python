# Aula 32: Flags, None e o operador is
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade) Comparar se é o mesmo objeto
id = Identidade
"""



condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Faça outra coisa')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)