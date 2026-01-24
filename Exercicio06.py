# Exercício 6 Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e raíz quadrada.

n1 = int(input('Digite um valor para devolver seu dobro, triplo e sua raiz quadrada possível: '))
print('Sabendo que o valor é {}, seu dobro é equivalente a {}, seu triplo igual a {}.\nLogo, sua raiz quadrada possível é {:.4f}.'.format(n1, n1*2, n1*3,n1**(1/2)))
