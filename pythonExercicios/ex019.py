import random
print('Sorteio de um aluno para apagar o quadro\nEscreva os nomes dos alunos:\n')
A = input('Aluno 1: ')
B = input('Aluno 2: ')
C = input('Aluno 3: ')
D = input('Aluno 4: ')
sorteio = [A, B, C ,D]
sorte = random.choice(sorteio)
print(f'O aluno sorteado foi: {sorte}')

