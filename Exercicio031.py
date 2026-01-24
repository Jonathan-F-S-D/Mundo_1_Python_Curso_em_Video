# Exercício 31 Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 KM e
# R$ 0,45 para viagens mais longas.

dist = float(input('Somos da empresa de passagens!\n\nDigite a distância em Km que percorrerá durante toda viagem: '))
if dist <= 200.00:
    print('Baseado na sua distância de {:.2f} Km, o preço total da passagem será de R$ {:.2f}'.format(dist, dist * 0.50))
else:
    print('Baseado na sua longa distância de {:.2f} Km, o preço total da passagem será de  R$ {:.2f}'.format(dist, dist * 0.45))

# Resposta Simplificada do Guanabara # 'if in line'/Operador Ternário
distancia = float(input('Digite a distância, em Km, de sua viagem: '))
print('Você está prestes a fazer uma viagem de {:.2f} Km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200.00 else distancia * 0.45   # Não é tão bom quando o anterior, mas funciona
print('O preço da passagem ficará em R$ {:.2f}'.format(preco))

