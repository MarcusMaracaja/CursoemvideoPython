n = 'ALUGA CAR'
print(' o/=|o- ' * 10)
print('{:^80}'.format(n))
print('=-' * 40)
p = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foi rodado? '))
dias = 60 * p
A = km * 0.15
print('O custo total do aluguel foi: R${:.2f}'.format(dias + A))
