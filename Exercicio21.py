# Exercício 21 Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
import winsound

winsound.PlaySound("*",winsound.SND_ALIAS) # Isso faz som, agora, eu quero um audio musical.
# Infelizmente, essa biblioteca é limitada aos sons disponíveis nela. Descobri isso depois de pesquisar o que ela pode e não fazer.

# Tentei instalar diversas Bibliotecas/Módulos de música. Porém, todos eles quebraram.
# Descobri que os Módulos são incompatíveis com a versão do meu Python.
# Dei um rolê do caralho. Foda-se o que eu fiz aqui, no final só precisei executar o Python 3.11 e, na própria IDE, instalar o 'pygame' porque o desgraçado do 'playsound' tá aviadado e não funciona mais.



## Modo Curso em video
import pygame
pygame.init()
pygame.mixer.music.load('ex021_TLOZ.wav')
pygame.mixer.music.play()
pygame.event.wait()

#### MODO JOJO e sua Pesquisa FODA

import pygame
pygame.mixer.init()
music1 = pygame.mixer.Sound('ex021_TLOZ.wav')

while True:
    tocar = input('Aperte qualquer coisa para sonorizar: ')
    music1.play()
    print('Tocando...')

