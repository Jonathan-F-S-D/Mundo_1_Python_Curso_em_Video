# Exercício 18 Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

angulo = float(input('Digite o valor de algum ângulo desejado: ')) # É necessário converter esse valor para Radianos
#math.radians()    # Convertendo para Radianos
sen = (sin(radians(angulo)))      # A sequência lógica é: O 'Ângulo' será transformado
cos = (cos(radians(angulo)))      # em radianos e será calculado para o seno, cosseno ou tangente)
tang = (tan(radians(angulo)))

print('O ângulo {:.2f}°, terá o SENO de {:.2f}'.format(angulo,sen))
print('O ângulo {:.2f}°, terá o COSSENO de {:.2f}'.format(angulo,cos))
print('O ângulo {:.2f}°, terá a TANGENTE de {:.2f}'.format(angulo,tang))

# Modo de achar os ângulos com os catetos e a Hipotenusa

from math import sqrt, pow
'''
print('\n\n\n Solução com CATETOS e HIPOTENUSA!')
print('Me forneça valores dos catetos para calcular a hipotenusa e os ângulos em Seno (30º), Cosseno (45°) e Tangente (60º)')
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
h = sqrt(pow(ca,2) + pow(co,2))
print('Com os valores, a HIPOTENUSA será igual a {:.2f}\n\n'.format(h))
print('Agora, podemos descobrir os ângulos.')
seno = co / h
cosseno = ca / h
tangente = seno / cosseno # ou Cateto oposto / Cateto Adjacente
print('Seno: {:.2f}°\nCosseno: {:.2f}°\nTangente: {:.2f}°'.format(seno, cosseno, tangente))
'''