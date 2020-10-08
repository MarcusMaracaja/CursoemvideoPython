print('lê um número inteiro e verifica se ele é par ou ímpar')
n = int(input('Digite um npumero: '))
r = n % 2
if r == 0:
    print('{} é par!'.format(n))
else:
    print('{}  é ímpar!'.format(n))
