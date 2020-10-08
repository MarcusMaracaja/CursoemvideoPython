import emoji
print(emoji.emojize(' :musical_note:'*25, use_aliases=True))
print('Maiusculas,minusculas, espaços e contagem')
print(emoji.emojize(' :earth_americas:'*25, use_aliases=True))
nome = (input('Escreva seu nome completo: '))
print('MAIÚSCULAS: {}\n'.format(nome.upper()))
print('minúsculas: {}\n'.format(nome.lower()))
sep = nome.split()
junto = ''.join(sep)
print('Seu nome completo tem: {} letras'.format(len(junto)))
print('Seu primeiro nome é {} e tem {} letras.'.format(sep[0].capitalize(), len(sep[0])))

