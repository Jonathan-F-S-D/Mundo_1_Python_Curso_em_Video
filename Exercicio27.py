# Exercício 27 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Digite seu nome completo: ')).title().strip().split()
print('Primeiro Nome: {}'.format((nome[0])))
print('Último Nome: {}'.format(nome[len(nome) -1]))