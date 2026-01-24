# Exercício 28 Escreva um programa que faça o computador "pensar" em um
# número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
import time

print('-=-' * 17)
print((' ' *5), 'Bem Vindo ao *JOGO DA ADIVINHAÇÃO*!!!', (' '*5),'\nTemos você e nossa máquina! Quem será o vencedor?')
print('-=-' * 17)
print('\nO jogo é simples. Nossa máquina escolherá um valor de 0 a 5\n', '-$-'*3, ' Se adivinhar, você vencerá! ', end= ('-$-'*3))
numero = int(input('\n\nAgora, escolha o seu número: '))   # Input do jogador
maquina = randint(0,5)      # Sorteio aleatório de um número
print('PROCESSANDO ...')
time.sleep(1.5)
if maquina == numero:             # Dois iguais REALMENTE quer dizer igual
    print('Parabéns. Você adivinhou o número!!!')
else:
    print('Nossa máquina venceu desta vez. Ela escolheu o {} e você o {}.\nTente novamente.'.format(maquina,numero))
