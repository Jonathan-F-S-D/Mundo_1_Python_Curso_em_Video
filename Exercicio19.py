# Exercício 19 Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# do escolhido.

from random import randint,choice
print('O professor escolheu 4 alunos da sua turma para apagar o quadro negro.\nAjude-o a sortear 1 deles.')
a1 = ('Mariazinha = 1')
a2 = ('Marcinha = 2')
a3 = ('Marcelinho = 3')
a4 = ('Maurinho = 4')
sorteio = randint(1, 4)
print('Entre os alunos: {}, {}, {} e {}, o professor sorteou o(a) aluno(a) com o número {}.'.format(a1, a2, a3, a4, sorteio))
###
print('\n\nEm outra sala de aula...')
a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))
sorte = choice([a,b,c,d])
print('O aluno escolhido para apagar o quadro foi o(a): {}.'.format(sorte))