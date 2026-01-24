# Exercício 9 Faça um programa que leia um número inteiro qualquer e mostre
# na tela a sua tabuada.

n = int(input('Digite qualquer valor aqui; farei a tabuada, do 0 ao 10, inteira dele.\n>>> '))
print('Tabuada do número {}:'.format(n))
print('-'*13 +'\n0 x {:^3} = {:^3}\n1 x {:^3} = {:^3}\n2 x {:^3} = {:^3}\n3 x {:^3} = {:^3}\n4 x {:^3} = {:^3}\n5 x {:^3} = {:^3}\n'
      '6 x {:^3} = {:^3}\n7 x {:^3} = {:^3}\n8 x {:^3} = {:^3}\n9 x {:^3} = {:^3}\n10 x{:^3} = {:^3}'.format(n,n*0,n,n*1,n,n*2,n,n*3,n,n*4,n,n*5,n,n*6,n,n*7,n,n*8,n,n*9,n,n*10)+ '-'*13)