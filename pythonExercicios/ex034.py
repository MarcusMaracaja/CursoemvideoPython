print('Calculo do valor do aumento de salário')
sal = float(input('digite o valor do seu salário atual: R$'))
if sal <= 1250.00:
    novo = sal * 15 / 100 + sal
    print('Seu salário terá um aumento de 15% e será R${:.2f}'.format(novo))
else:
    novo = sal * 10 / 100 + sal
    print('Seu salário terá um aumento de 10% e será R${:.2f}'.format(novo))
