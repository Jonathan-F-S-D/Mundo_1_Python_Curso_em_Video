# Exercício 8 Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetro e milímetros.

print('Abaixo, coloque um valor, inteiro ou quebrado, e ele será convertido em metros, centímetros e milímetros')
valor1=float(input('>>> '))
print('Seu valor impresso foi {:.2f}. Agora, segue as conversões:\nMetros: {:.2f} m\n'
      'Centímetros: {:.2f} cm\nMilímetros: {:.2f} mm'.format(valor1,valor1*1,valor1*100,valor1*1000))
#Metros é um valor simples = 3.00
#Centímetros faz o mesmo possuir 2 zeros, indo para a casa da dezena = 300.00
#Milímetros transforma este valor acima, para a casa dos milhares, com mais um zero = 3.000.00

# Exercício aprimorado com quilômetro (km - 1000) / hectômetro (hm - 100) / decâmetro (dam - 10) /
# Metros (m - 1.0) / decímetro (dm - 0.1) / Centímetro (cm - 0.01) / milímetro (mm - 0.001)

num = float(input('Digite um valor para todas as medidas: '))
km = num / 1000
hm = num / 100
dam = num / 10
m = num
dm = num * 10
cm = num * 100
mm = num * 1000
print('Kilômetro = {:.4f}\nHectômetro = {:.3f}\nDecâmetro = {:.2f}\n'
      'Metro = {}\nDecímetro = {}\nCentímetro = {}\nMilímetro = {}'.format(km,hm,dam,m,dm,cm,mm))
