# Exercício 24 Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "SANTO".
cidade = str(input('Digite o nome de uma cidade: '))
dividido = cidade.split()[0]
C_alta = dividido.upper()
print('Sua cidade possuo SANTO no início de seu nome? {}'.format('SANTO'in(C_alta)))

## Solução Guanabara
cid = str(input('Digite sua Cidade: ')).strip()
print('Sua cidade tem santo no nome? {}'.format(cid[:5].upper() =='SANTO'))

## Sempre pense que o usuário fará besteira ao digitar; solucione problemas futuros.


