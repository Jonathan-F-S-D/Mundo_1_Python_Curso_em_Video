# Exercício 10 Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos DÓLARES ela pode comprar
        # Considere US$ 1.00 = R$ 3.27

valor = float(input('Olá! Sou sua carteira digital!\n\nInsira um valor para saber quantos dólares você pode adquirir.\n(Conversão: US$ 1.00 = R$ 3.27)\n>>>R$ '))
dolar = valor / 3.27
iene = valor / 0.034 #hoje em dia
euro = valor / 6.29
print('Com o valor posto, de R$ {:.2f} reais, é possível adquirir US$ {:.2f} dólares'.format(valor, dolar))
print('\nVeja mais opções também:\nEuro: EUR $ {:.2f} | Yen: JPL $ {:.2f}'.format(euro,iene))
print(('-'*5) +'Info: 08/01/2026' +('-'*5))