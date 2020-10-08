import math
print('Leia os catetos e calcule a hipotenusa')
co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente? '))
h = math.sqrt(ca**2 + co**2)
print('O tamanho da hipotenusa é: {:.2f}'.format(h))

