# Exercício 12 Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.


produto = str(input('Calcularei o preço novo de um produto na promoção de 5% de desconto!\nDigite o nome de um produto: '))
valor = float(input('Digite o preço deste produto: R$ '))
# Cálculos de porcentagem são fáceis quando se converte a porcentagem.
# No caso, temos 5%. logo teremos 0.05 (100% = 1.00 | 10% = 0.1 | 1% = 0.01)
desconto = valor*0.05
print('O produto {}, com desconto de 5%, sairá por {:.2f}'.format(produto,(valor-desconto)))

# É possível, para além de saber os valores da porcentagem em números reais, realizar a seguinte ideia:
# "valor' * 'desconto' / 100 (%).
# Em nosso caso, valor*5/100