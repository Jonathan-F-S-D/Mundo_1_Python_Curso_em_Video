# Exercício 5 Faça um programa que leia um número inteiro e mostre na tela
# o seu sucessor e seu antecessor.

n1 = int(input('\033[1;31;44mDigite um valor para mostrar-lhes seu sucessor e seu antecessor: \033[m'))
print('O valor posto é este: \033[33m{}\033[m. Logo, seu antecessor é \033[35m{}\033[m e seu sucessor é \033[35m{}\033[m.' .format(n1, n1-1, n1+1))
