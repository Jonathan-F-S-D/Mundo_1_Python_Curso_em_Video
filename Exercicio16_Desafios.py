# Exercício 16 Crie um programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
# EX: Digite um número: 6.127  |  O número 6.127 tem a parte inteira 6.
# Para comentar todo o código, coloque três aspas em sequência, e mais três no final

from math import trunc

num = float(input('Digite um valor qualquer, com casas decimais, para especificações: '))
print('Seu número é {} e sua Porção Inteira é {}'.format(num,trunc(num)))

# Existe uma segunda forma de realizar esta atividade, sem necessidade de importar nenhum Módulo

n = float(input('Digite um valor: '))
print('Seu número é {} e a parte inteira é {}'.format(n, int(n))) # É possível definir antes de apresentar.