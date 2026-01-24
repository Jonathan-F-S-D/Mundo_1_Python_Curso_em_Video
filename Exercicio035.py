# Exercício 35 Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.

print('Teste de medidas!!\n\nDiga-me três medidas e eu retornarei a ti se estas podem formar um triângulo.')
m1 = float(input('Digite a primeira medida: '))
m2 = float(input('Digite a segunda medida: '))
m3 = float(input('Digite a terceira medida: '))
if (m1 + m2) > m3 and (m1 + m3) > m2 and (m2 + m3) > m1:
    print('\nCom suas medidas, é possível formar um triângulo!')
else:
    print('\nCom suas medidas, infelizmente, é IMPOSSÍVEL formar um triângulo.')


