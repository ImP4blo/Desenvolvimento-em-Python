"""
Interando strings com while
"""

# ..... 0123456789101112
nome = 'Pablo Mateus' # Interáveis

tamanho_nome = len(nome)
# print(nome[0])
# print(tamanho_nome)

asterisco = '*'
resultado = ''
indice = 0

while indice < tamanho_nome:
    resultado += nome[indice] + asterisco
    indice += 1
print(asterisco + resultado)

# ---------------------------------------------------------------
# Versão do professor (para comparar com a minha)
# ---------------------------------------------------------------
# indice = 0
# novo_nome = ''
# while indice < len(nome):           # usa len() direto, sem variável extra
#     letra = nome[indice]            # guarda a letra da vez numa variável
#     novo_nome += f'*{letra}'        # f-string: asterisco ANTES da letra
#     indice += 1
#
# print(novo_nome)
#
# Diferenças em relação à minha versão:
# - f'*{letra}' faz o mesmo que asterisco + letra, mas em uma única string.
# - A variável "letra" deixa o código mais legível (nome[indice] tem nome).
# - Saída dele: *L*u*i*z* *O*t*á*v*i*o -> NÃO tem o * no final.
#   A minha termina com *, porque somei mais um asterisco no print.

# resultado esperado e alcançado! -> *P*a*b*l*o* *M*a*t*e*u*s*