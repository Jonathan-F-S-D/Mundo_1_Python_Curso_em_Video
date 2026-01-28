#4 Faça um programa que leia algo pelo teclado e mostre na tela o seu
#  tipo primitivo e todos as possíveis informações sobre ele.
print("O código abaixo estará mostrando 'False' (Falso) e 'True' (Verdadeiro)")
print()
n = input('\033[1;33mDigite algo aqui: \033[m')
print("Primeiramente, ele é:", type(n), ", sendo da classe texto.")
print("\033[37mO digitado é um número/letra?", n.isnumeric())
print("É uma Letra?", n.isalpha())
print('\033[35mEstá em caixa baixa?', n.islower())
print('Está em Caixa alta?', n.isupper())
print('\033[31mÉ um dígito?', n.isdigit())
