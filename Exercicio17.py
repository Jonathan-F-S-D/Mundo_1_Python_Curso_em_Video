# Exercício 17 Faça um programa que leia o cateto oposto e do cateto
# adjacente de um triângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = sqrt(pow(co,2) + pow(ca,2))
print('A hipotenusa será {:.2f}.'.format(h))

# Existe o modo sem o Módulo
caa= float(input('Comprimento do cateto adjacente: '))
coo= float(input('Comprimento do cateto oposto: '))
hi = (caa ** 2 + coo ** 2) ** (1/2)
print('A Hipotenusa é: {:.2f}.'.format(hi))

# Ainda aqui, existe a função da Hipotenusa dentro do Módulo math
from math import hypot
cta = float(input('Diga o cateto adjacente: '))
cto = float(input('Diga o cateto oposto: '))
hipo = hypot(cto, cta)
print('O resultado da hipotenusa será {:.2f}.'.format(hipo))
