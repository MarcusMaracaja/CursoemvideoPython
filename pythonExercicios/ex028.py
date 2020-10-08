import random
from time import sleep
pc = random.randint(0, 5)
u = int(input('Tente adivinhar entre 0 e 5, qual foi o número que o computador escolheu: '))
print('Processando...')
sleep(3)
if pc == u:
    print('Acertou mizeravi!')
else:
    print('ERROU!')
print('====FIM====')
