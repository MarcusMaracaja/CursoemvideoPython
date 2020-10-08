print('Calcula o preço da passagem')
d = float(input('Qual é a distância que vc vai viajar? '))
if d <=200.0:
    p = d * 0.50
    print('Para uma viajem curta de {:.2f}km, o valor da passagem será R${:.2f}'.format(d, p))
else:
    p = d * 0.45
    print('Para uma viajem longa de {:.2f}km, o valor da passagem será R${:.2f}'.format(d, p))
print('Boa viajem!')