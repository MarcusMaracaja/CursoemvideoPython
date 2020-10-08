print('Lê o nome de uma cidade e diz se ela tema  palavra santo')
cidade = input('Escreva o nome de sua cidade: ')
cidade = cidade.title()
tem = cidade.find('Santo')
print(cidade)
if tem != -1:
    print('A cidade  com Santo! Parabéns!')
else:
    print('Cidade sem Santo!')


