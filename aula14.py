a = 'A'
b = 'B'
c = 1.1

string = 'a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'

# .format é um método de string que permite inserir valores em uma string de forma organizada. Ele substitui os placeholders {} pelos valores fornecidos na ordem em que aparecem.
formato = string.format(
    nome1 = a, 
    nome2 =b,
    nome3 = c) 

print(formato)