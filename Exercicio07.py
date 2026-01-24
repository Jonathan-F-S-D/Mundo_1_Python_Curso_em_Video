# Exercício 7 Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre sua média.

nota1 = float(input('Digite o valor da primeira nota do aluno: '))
nota2 = float(input('Digite o valor da segunda nota do aluno: '))
print('O aluno recebeu pontuações de 0 a 10 em suas provas.\nNa primeira, conseguiu {} pontos; na segunda recebeu {}.\nLogo, sua média final é {:.3f}'.format(nota1, nota2, (nota1+nota2)/2))
