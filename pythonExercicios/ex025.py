print('Lê o nome de uma pessoa e diga se ela tem SILVA no nome')
nome = input('Escreva seu nome completo: ')
nome = nome.title()
tem = nome.find('Silva')
if tem != -1:
    print('Parabéns, Silva é uma grande Família')
else:
    print('Você não faz parte da família Silva')
