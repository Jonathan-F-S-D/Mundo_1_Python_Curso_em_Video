#3 Crie um Script em Python que leia dois números e tente mostrar a soma entre eles.

print('\033[1;31;46mEste é um script para somar dois valores distintos! Então, me forneça dois valores.\033[m')
valor1 = input('\033[1mValor 1: ')
valor2 = input('Valor2: \033[m')
soma = int (valor1) + int (valor2)

print('\033[1;31;46mA soma dos valores fornecidos é igual a: \033[m', soma)

# forma 2

print('Este é um script para somar dois valores distintos! Então, me forneça dois valores.')
valor1 = int(input('\033[1mValor 1: '))
valor2 = int(input('Valor2: \033[m'))
soma = valor1 + valor2

print('A soma dos valores fornecidos é igual a: ', soma)

#3.0 Somar dois valores e mostrar tudo mastigado na tela

vl1 = int(input('Digite um valor: '))
vl2 = int(input('Digite outro valor: '))
s = vl1 + vl2
#print('A soma entre ',vl1,' e ',vl2,' é igual a ',s)
print('\033[36mA soma entre {} e {} é igual a {}'.format(vl1,vl2,s))
