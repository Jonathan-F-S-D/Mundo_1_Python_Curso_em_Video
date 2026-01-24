# Exercício 34 Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00 calcule um aumento de 10%

# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Reajustador de salário!\n\nDigite seu salário atual: R$ '))
if salario > 1250.00:
    print('Com o reajuste de 10%, seu novo salário será de R$ {:.2f}'.format((salario * 0.1)+salario))
else:
    print('Com reajuste de 15%, seu novo salário passará a ser de R$ {:.2f}'.format((salario * 0.15) + salario))