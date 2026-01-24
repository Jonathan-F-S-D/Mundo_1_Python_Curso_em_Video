#4 Faça um programa que leia algo pelo teclado e mostre na tela o seu
#  tipo primitivo e todos as possíveis informações sobre ele.
print("O código abaixo estará mostrando 'False' (Falso) e 'True' (Verdadeiro)")
print()
n = input('Digite algo aqui: ')
print("Primeiramente, ele é:", type(n), ", sendo da classe texto.")
print("O digitado é um número/letra?", n.isnumeric())
print("É uma Letra?", n.isalpha())
print('Está em caixa baixa?', n.islower())
print('Está em Caixa alta?)', n.isupper())
print('É um dígito?', n.isdigit())