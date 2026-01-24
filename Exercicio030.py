# Exercício 30 Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

num = int(input('Digite um número inteiro para identificarmos ele: '))
if num % 2 == 0:                    # A ideia é, 0 será PAR e 1 será ÍMPAR pelo Resto da Divisão.
    print('Seu número é PAR!')
else:
    print('Seu número é ÍMPAR!')