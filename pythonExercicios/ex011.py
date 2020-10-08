print('Calcula quanto de tinta de gasta numa parede de acordo com a sua área')
n1 = float(input('Digite a largura da parede em metros: '))
n2 = float(input('Digite a altura da parede em metros: '))
area = n1 * n2
print('Considerando que a tinta 2m²/l...')
print('Você gastará {:.2f} litros para pintar {:.2f}m² de parede.'.format(area/2, area))