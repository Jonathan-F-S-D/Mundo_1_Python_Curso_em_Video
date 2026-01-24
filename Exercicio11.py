# Exercício 11 Faça um programa que leia a largura e a altura de uma parede
# em metros. Calcule sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

print('Assistente de tinta ativado!\nForneça-me a largura e a altura de sua parede para sabermos quantos baldes de tinta você precisará!\n'
      '(Cada balde de tinta cobrirá 2m²)\n')
largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
area = largura * altura
print('\nO cálculo da área se dará da seguinte equação: Largura {:.2f} x Altura {:.2f}.'.format(largura, altura))
print('A área da sua parede têm {:.2f}m².\n\nSabendo-se que sua parede possui {:.2f}m de altura e {:.2f}m de largura.'
      '\nVocê precisará de {:.2f} Litro(s) de tinta.'.format(area,altura,largura,(area/2)))