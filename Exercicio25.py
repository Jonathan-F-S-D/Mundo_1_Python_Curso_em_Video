# Exercício 25 Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome inteiro: ')).strip()
print('O seu nome possui SILVA?\nTrue ou False (Verdadeiro ou Falso): {}\nSua posição é igual a {}.'.format('SILVA'in(nome).upper(), nome.upper().find('SILVA')))