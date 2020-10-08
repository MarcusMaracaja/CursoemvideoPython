import math
print('Lê o comprimento de 3 retas e dis se forma um triângulo')
print('▲'*40)
print('''Para construir um triângulo não podemos 
utilizar qualquer medida, tem que seguir a condição 
de existência:
Para construir um triângulo é necessário que a medida 
de qualquer um dos lados seja menor que a soma das 
medidas dos outros dois e maior que o valor absoluto 
da diferença entre essas medidas.''')
print('▲'*40)
print('Escreva as medias dos lados A, B, C:')
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))
if abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b):
    print('▲Forma triângulo▲')
else:
    print('Não forma triângulo')
