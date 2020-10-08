v = float(input('Qual foi a velocidade que o carro passou pela lmbada eletrônica?\n '))
if v > 80.0:
    print('você foi multado!')
    multa = (v - 80.0) * 7.00
    print('Sua multa é de: R${:.2f}'.format(multa))
else:
    print('Dentro do limite.')
print('-----FIM-----')
