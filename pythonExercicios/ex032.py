import datetime
print('Mostra se o ano é bissexto!')
print("""Para um ano ser bissexto, sua dezena precisa
ser múltiplo de 4 e se for um ano terminado em 00,
precisa ser múltiplo de 400, vejamos:""")
ano = int(input('Digite o ano (0 para o ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
    print('O ano atual é {}'.format(ano))
u = ano // 1 % 10
d = ano // 10 % 10
c = ano // 100 % 10
dez = d*10 + u
cond1 = dez % 4  #se é 0 é multiplo é bisexto
if cond1 == 0:
    if dez == 0:
        cen = c * 100
        cond2 = cen % 400  # se é 0 é multiplo é bisexto
        if cond2 == 0:
            print('{} é bissexto!'.format(ano))
        else:
            print('{} não é bissexto!'.format(ano))
    else:
        print('{} é bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))
