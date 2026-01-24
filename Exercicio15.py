# Escreva um programa que pergunte a quantidade de KM
# percorridos por um carro alugado e a quantidade de
# DIAS pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0.15 por Km rodado.

print('Este é um aluguel de carros digital!\nInsira os dados requisitados de seu carro alugado!')
dia = int(input('Insira o valor de dias que ficaste com o carro.\nObs: Dias completos apenas\n>>> '))
km = float(input('Insira a kilometragem final do seu carro alugado em KM.\n>>> '))

diaPreço = (dia * 60)
kmPreço = (km * 0.15)
print('*Tabela final do aluguel de carros*\n' + ('-'*40) + '\nCusto pelos {} dias: R$ {:.2f}'.format(dia,diaPreço))
print('Custo pelos {:.2f} km rodados: R$ {:.2f}\nPreço final: R$ {:.2f}'.format(km,kmPreço,(diaPreço+kmPreço)))