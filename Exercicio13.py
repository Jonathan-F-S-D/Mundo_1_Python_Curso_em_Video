# Exercício 13 Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário com 15% de aumento.


funcionario = ('Jonathan Feliz')
salario = float(input('O funcionário {}, que trabalhará no T.I precisará de um salário.\nDigite seu salário aqui: R$ '.format(funcionario)))
aumento = salario*0.15
print('Com este salário R$ {:.2f}, e se enquadrando dentro do aumento salarial de 15% obrigatórios,\n{} receberá R$ {:0.2f}.'.format(salario, funcionario, (salario + aumento)))
