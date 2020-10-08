print('Lê um número e mostra sua tabuada')
n1 = int(input('Digite um número inteiro: '))
print('Tabuada de {}:\n'.format(n1))
h = int
for h in range(0, 11):
    print('{} X {} = {}'.format(n1, h, h*n1))
