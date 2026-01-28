#2 - Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa
#    e mostre uma mensagem com a data formada.

print('\033[33mBem-vindo, pessoa! Me diga o dia, mês e ano do seu nascimento para que eu os formate para ti!\033[m')

ano = input('Qual o ano de seu Nascimento? ')
mes = input('Qual seu mês de Nascimento (escreva por extenso)? ')
dia = input('Qual sua data de Nascimento? ')

print('\033[7;42mEntão, você nasceu no dia ' + dia + ' de ' + mes + ' em ' + ano + '!\033[m')
