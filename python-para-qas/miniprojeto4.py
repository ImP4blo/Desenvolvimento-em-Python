

senha_secreta = 'python123'

senha_digitada = ""

while senha_digitada != senha_secreta:
    print("--- Sistema de Segurança ---")
    senha_digitada = input('Digite a senha: ')

    if senha_digitada == senha_secreta:
        print('Acesso permitido!')

    else:
        print('Acesso negado!')


print('Fim do programa.')