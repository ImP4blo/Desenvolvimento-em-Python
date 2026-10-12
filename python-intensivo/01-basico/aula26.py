"""
Formatação básica de string
s - string
d - int
f - float
.<número de dígitos>f
x o X - Hexadecmal
(caractere) (><^) (quantidade)
> - esquerda
< - direita
^ - centro
= - força o número a aparecer antes dos zeros
Sina - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
!r - repr
!s - str
!a - ascii
"""

variavel = 'ABC'
print(f'{variavel}') 
print(f'{variavel: >11}') 
print(f'{variavel: <11}') 
print(f'{variavel:!^11}') 
print(f'{1000.456165161657:0=+10,.1f}') 
print(f'O hexadecimal de 1500 é {1500:08X}')