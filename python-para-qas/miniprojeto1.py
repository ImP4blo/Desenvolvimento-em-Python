

# Todo - Interação basica com o usuáro
print("--- Bem-vindo ao Sistema de Cadastro ---")

# 1 passo - Pergunta os dados
nome = input('Qual se nome? ' )
comida = input('Qual sua comida favorita? ' )
cidade = input('Qual a ultima cidade em que vc comeu sua comida favorita? ')

# 2 passo - Exibe os resultados
print(f'olá, {nome}! Sua comioda favorita é {comida} e a ultima vez que vc comeu foi em {cidade}!')

print('Resumindo')
print(f'nome: {nome}')
print(f'comida favorita: {comida}')
print(f'cidade: {cidade}')