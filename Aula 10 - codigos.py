### Código com IF - sem Else (Estrutura simples)
nome = str(input('Digite seu nome: '))
if nome == 'Jonathan':
    print('Seu nome é lindo!')
print('Bom dia, {}!'.format(nome))


### Código com Ambos (Estrutura Composta)

nome = str(input('Digite seu nome: '))
if nome == 'Jonathan':
    print('Seu nome é lindo!')
else:
    print('Seu nome é tão comum!')
print('Bom dia, {}!'.format(nome))

###  TESTE EM CONTAS ###

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('Sua média é {:.1f}'.format((n1 +n2)/2))
if (n1+n2)/2 >= 6.0:
    print('Parabéns! Você passou de ano!')
else:
    print('Você terá muito tempo para estudar...\n Você REPROVOU')

### CONDIÇÃO SIMPLIFICADA ###
print('Parabéns'if (n1+n2)/2 >= 6.0 else 'Estude MAIS')