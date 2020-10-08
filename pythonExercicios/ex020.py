import random
print('Sorteia uma ordem de apresentação de trabalhos\nDigite o nome dos alunos: ')
A = input('Aluno 1: ')
B = input('Aluno 2: ')
C = input('Aluno 3: ')
D = input('Aluno 4: ')
l = [A, B, C, D]
random.shuffle(l)
print('A ordem dos alunos é: {}'.format(l))
