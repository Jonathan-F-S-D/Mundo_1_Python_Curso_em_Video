# Exercício 20 O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
# a ordem de apresentação.

from random import shuffle
print('O professor escolheu quatro alunos, Lucas, Ismael, Diego e Jonathan, para apresentar trabalhos.\nEle fará um sorteio da sequência das apresentações.')
lista = ['Lucas','Ismael','Diego','Jonathan']
shuffle(lista)       # Seleciona a "lista" referenciada e retorna, randomicamente, suas posições em sequência.
print('Por fim, o sorteio aconteceu e as apresentações, em sequência ficarão assim: {}'.format(lista))

# Não Consegui 11 01 2026
# Consegui. 12 01 2026. Não era com a função 'choices()'
# Tive que ler no w3schools para saber o que a biblioteca 'random' permitia-me.

###
print('\n\nEm outra sala de aula...')
a = str(input('Diga um nome: '))
b = str(input('Diga mais um: '))
c = str(input('Ainda faltam dois: '))
d = str(input('Por último, mas um aluno: '))
lista1 = [a,b,c,d]
shuffle(lista1)         # Fique atento com o tipo de referência
print('*misturando os nomes*\n\nAs apresentações ocorrerão nesta ordem: {} '.format(lista1))