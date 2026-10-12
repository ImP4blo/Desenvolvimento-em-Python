
print("Bem-vindo ao sistema de cadastro!")


cadastro = {}

cadastro['nome'] = input('digite seu nome: ')
cadastro['comida'] = input('digite sua comida favorita: ')
cadastro['cidade'] = input('digite sua cidade: ')

print('\n' + '=' * 30)
print("Ficha de dados")
print("="*30)

for chave, valor in cadastro.items():
    print(f'{chave.capitalize()}: {valor}')
