# Aula 13: f-strings
nome = 'Pablo Mateus'
altura = 1.77
peso = 117
imc = peso / altura ** 2

# Pablo Mateus tem 1.77 de altura, 
# pesa 117 quilos e seu imc é


# f-strings (formatação de strings) - Python 3.6+
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)