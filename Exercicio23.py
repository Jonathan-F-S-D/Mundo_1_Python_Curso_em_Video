# Exercício 23 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# EX: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
# (Receber respostas textualmente e matematicamente)

### SOLUÇÃO TEXTUAL

num = str(input('Digite um número inteiro entre 0 e 9999: ')).zfill(4)          # LEIA A DOCUMENTAÇÂO DO PYTHON SEMPRE QUE FICAR PRESO.
print('Essas são as características do número: {}'.format(num))
print('Unidade: {}\nDezena: {:>2}\nCentena: {}\nMilhar: {:>2}'.format(num[3], num[2], num[1], num[0]))

### SOLUÇÃO NUMÉRICA

n = int(input('Digite um valor entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10   # poderia ser n // 10 // 10 % 10
m = n // 1000 % 10  # poderia ser n // 10 // 10 // 10 % 10
print('Unidade: {:>4}\nDezena: {:>5}\nCentena: {:>4}\nMilhar: {:>5}'.format(u, d, c, m))
