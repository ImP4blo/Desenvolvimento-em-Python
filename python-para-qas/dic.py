

pessoa = {
    'nome': 'Pablo',
    'idade': 25,
    'profissão': 'QA Engineer',
    'ativo': True
}

# print(pessoa ['nome'])

pessoa['idade'] = 26

pessoa['profissão'] = 'Senior QA Engineer' 

# print(pessoa)


# for chave in pessoa:
#     print(chave)


for chave, valor in pessoa.items():
    print(f'A chave {chave} guarda o valor {valor}')