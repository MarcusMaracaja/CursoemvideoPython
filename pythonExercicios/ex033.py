import math
print('Qual é o maior dentre três números DIFERENTES e inteiros?')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 == n2 or n1 == n3 or n2 == n3:
    print('==========ERRO!==========\nDigite números diferentes!')
else:
    if n1 > n2 > n3:
        print('{} é o maior e {} é o menor.'.format(n1, n3))
    if n1 > n3 > n2:
        print('{} é o maior e {} é o menor.'.format(n1, n2))
    if n2 > n1 > n3:
        print('{} é o maior e {} é o menor.'.format(n2, n3))
    if n2 > n3 > n1:
        print('{} é o maior e {} é o menor.'.format(n2, n1))
    if n3 > n1 > n2:
        print('{} é o maior e {} é o menor.'.format(n3, n2))
    if n3 > n2 > n1:
        print('{} é o maior e {} é o menor.'.format(n3, n1))



