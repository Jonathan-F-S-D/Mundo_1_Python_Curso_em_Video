# Exercício 22 Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas minúsculas.
# Quantas letras ao todo (Sem contar os espaços).
# quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')) # se colocar .strip() aqui no final, fica show
print('Caixa Alta: {}'.format(nome.upper()))
print('Caixa Baixa: {}'.format(nome.lower()))
separado = nome.split()
print('Seu nome com espaços tem {} posições. Sem eles, resulta em {} posições'.format(len(nome),len(''.join(separado))))
print('Seu primeiro nome ({}) possue {} posições'.format(nome.split()[0],len(separado[0])))

## versão Guanabara

nome = str(input('Digite seu nome completo: ')).strip()
print('Caixa Alta: {}'.format(nome.upper()))
print('Caixa Baixa: {}'.format(nome.lower()))
print('Letras, sem espaços, ao todo: {}'.format(len(nome) - nome.count(' ')))
#separadao = nome.split()
#print('Seu primeiro nome, {}, tem {} letras.'.format(separado[0], len(separado[0])))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))    # Aqui, o '.find' encontra o primeiro espaço, e retorna tudo antes dele

