#3 Crie um Script em Python que leia dois números e tente mostrar a soma entre eles.

print('Este é um script para somar dois valores distintos! Então, me forneça dois valores.')
valor1 = input('Valor 1: ')
valor2 = input('Valor2: ')
soma = int (valor1) + int (valor2)

print('A soma dos valores fornecidos é igual a: ', soma)

# forma 2

print('Este é um script para somar dois valores distintos! Então, me forneça dois valores.')
valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor2: '))
soma = valor1 + valor2

print('A soma dos valores fornecidos é igual a: ', soma)

#3.0 Somar dois valores e mostrar tudo mastigado na tela

vl1 = int(input('Digite um valor: '))
vl2 = int(input('Digite outro valor: '))
s = vl1 + vl2
#print('A soma entre ',vl1,' e ',vl2,' é igual a ',s)
print('A soma entre {} e {} é igual a {}'.format(vl1,vl2,s))