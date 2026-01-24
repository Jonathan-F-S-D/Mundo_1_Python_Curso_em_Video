# Exercício 33 Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

print('Vamos Brincar um pouco! Me diga três números que eu lhe falarei qual deles é o maior e qual é o menor.')
n1 = int(input('Digite o primeiro: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o último: '))
if n1 > n2 and n1 > n3:
    print('Entre os três, o maior número é o {}'.format(n1))
    if n2 < n1 and n2 < n3:
        print('Menor número: {}'.format(n2))
    elif n3 < n2 and n3 < n1:
        print('Menos número: {}'.format(n3))
    else:
        print('Demais valores são iguais.')
elif n2 > n1 and n2 > n3:
    print('Entre os três, o maior número é o {}'.format(n2))
    if n1 < n2 and n1 < n3:
        print('Menor número: {}'.format(n1))
    elif n3 < n1 and n3 < n2:
        print('Menor número: {}'.format(n3))
    else:
        print('Ambos valores restantes são equivalentes.')
elif n3 > n1 and n3 > n2:
    print('Entre os três, o maior número é o {}'.format(n3))
    if n1 < n2 and n1 < n3:
        print('Menor número: {}'.format(n1))
    elif n2 < n1 and n2 < n3:
        print('Menor número: {}'.format(n2))
    else:
        print('Ambos os outros valores são iguais. Não há superiores nem inferiores.')
else:
    print('Todos os valores são iguais!')

# Guanabara // Não há distinção entre valores iguais.
a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))