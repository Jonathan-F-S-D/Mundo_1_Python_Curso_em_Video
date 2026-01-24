# Exercício 32 Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Digite qualquer ano que lhe direi se este é ou não bissexto\n(0 = ano atual) >>> '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):       # o sinal '!=' significa "DIFERENTE DE"
    print('Sim. {} é um ano BISSEXTO.'.format(ano))
else:
    print('Não. {} NÃO é um ano BISSEXTO.'.format(ano))
