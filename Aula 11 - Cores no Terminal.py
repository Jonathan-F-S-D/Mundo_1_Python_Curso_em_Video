'''             CORES NO TERMINAL

    "Não é uma funcionalidade essencial para se ter, mas é muito maneiro poder fazer."

    Para os avançados, existe a Biblioteca/Módulo 'colorize', para desbloquear todas as cores.
    Porém, para iniciar no mundo das colorações, vamos utilizar funções do padrão ANSI

### * ANSI *
    É um padrão de normalização internacional. Ele possui 'escape sequence'.

    Este 'escape sequence' funciona em muitos ambientes. Em nosso caso, utilizaremos ele
    em nosso terminal, a fim de mudar a cor apenas no terminal apresentado.


####    Como funciona o código ANSI para cores?

    O código ANSI começa com contrabarra (\) e depois o código propriamente dito.
    Um desses códigos é o '033'. Ele possui algumas cores, limitadas, formatações e cores de fundo.

    O código é simbolizado assim:
    \033[m          ## Sim, o código será fechado pela letra 'm'.
                    ## Entre o colchete e o 'm' haverá os valores que você poderá digitar.

    estilo/fonte                    cor/letra               cor/fundo
     0 = Padrão IDE                 30 = Padrão IDE         40 = Padrão IDE
     1 = Negrito                    31 = Vermelho           41 = Vermelho
     4 = Sublinhado                 32 = Verde              42 = Verde
     7 = Inverte cor                33 = Amarelo            43 = Amarelo
         da letra e fundo           34 = Azul               44 = Azul
                                    35 = Lilás              45 = Lilás
                                    36 = Ciano              46 = Ciano
                                    37 = Cinza              47 = Cinza

                        Especial:   29 = Branco             39 = Branco
OBS: Se colocar nada, no lugar do Padrão IDE (qualquer coluna), a cor será branca.
OBS_2: O Padrão IDE, no meu pc, é MEIO BRANCO.
OBS_3: Como os valores são distintos (casa da unidade, 30 e 40), não há problemas em não adicionar o valor de algum
OBS_4: Caso utilize os três Modos, separe-os com ponto e vírgula ';', na ordem que quiser.

Vamos fazer alguns testes
'''
# Texto branco com fundo vermelho
print('\033[41mTeste')

# Texto amarelo, sublinhado e com fundo azul
print('\033[4;33;44mTeste')

#Texto lilás, em negrito, no fundo amarelo
print('\033[1;35;43mTeste')

# Texto cinza no fundo preto
print('\033[37;40mTeste')

# Texto branco no fundo preto, porém invertido
print('\033[7;30;39mTeste')
print('\033[m') # Cancela as cores
'''
        É possível realizar o mesmo código de várias formas
        
        * Pesquisar, Mais tarde, o módulo 'colorize'
          
'''
# DELIMITANDO AS CORES - COMEÇO E FIM
print('Eu quero sorvete de \033[1;30;44mbaunilha\033[m com \033[31mmorango\033[m!')

# DELIMITANDO AS CORES - CHAVES
nome = 'Jonathan'
print('Eu queria um amigo chamado {}{}{} !!!'.format('\033[1;35m', nome, '\033[m'))

# DELIMITANDO AS CORES - LISTA + CHAVES
dia = '24'
mes = 'Janeiro'
ano = 2026
cores = {'Limpa':'\033[m', 'Azul':'\033[1;34m', 'Amarelo':'\033[4;33m', 'Inverso-PB':'\033[7;29;40m'}
print('Concluí o curso Python 3 - Mundo 1, do \033[35mGuanabara\033[0m, no dia {}{}{} de {}{}{}, {}{}{}!!!'
      .format(cores['Azul'], dia, cores['Limpa'], cores['Amarelo'], mes, cores['Limpa'], cores['Inverso-PB'], ano, cores['Limpa']))

### DESAFIO DA AULA 11 _ COLOCAR, EM TODOS OS 35 EXERCÍCIOS, CORES.
'''
    Seguimentos que farei
    1 - 5 = Cores, começo e fim                     EASY
    6 - 10 = Cores com Chaves                       MEDIUM
    11 - 30 = Cores com Lista e Chaves              NORMAL
    30 - 35 = Utilizar o Módulo 'colorize'          HARD
'''