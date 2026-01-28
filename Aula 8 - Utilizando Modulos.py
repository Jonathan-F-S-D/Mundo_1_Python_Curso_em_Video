# UTILIZANDO MÓDULOS - BIBLIOTECAS

#               * O que são módulos? *
#   Módulos são "Adicionais" que te permite realizar novas funções
#   Dessa forma, módulos podem ser bibliotecas inteiras para Python (e em outras linguagens).

#   Para resgatar uma Biblioteca, usamos o 'import'.
import math             #Este é um exemplo de importação de uma biblioteca.

# É possível importar apenas algumas funcionalidades do Módulo, com o comando abaixo
from math import pow    #Com este comando, você importa algo específico do Módulo.import

# FOCANDO NO MÓDULO 'MATH'

# Abaixo, algumas das funcionalidades existentes no Módulo math

#math.ceil()         # Arredonda valores para cima
#math.floor()        # Arredonda valores para baixo
#math.trunc()        # Remove valores depois da vírgula, permanecendo valores Inteiros
#math.pow()          # Comando para potência
#math.sqrt()         # Comando para descobrir raíz quadrada
#math.factorial()    # EX: Fatorial de 5 (5!) é igual a: 5x4x3x2x1 = 120

#
# EXERCÍCIOS E TESTES
#
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raíz quadrada de {} é igual a {}.'.format(num,raiz))

## Arredondamento para cima ou baixo
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raíz quadrada de {} é igual a {}, para cima, e {}, para baixo.'.format(num,math.ceil(raiz),math.floor(raiz)))

# Caso você utilize a busca de um módulo específico com from math import sqrt
# Você poderá escrever, no seu código, apenas o nome da função, sem referenciar seu módulo.

from math import sqrt,floor
num = int(input('Digite um valor lindo: '))
raiz = sqrt(num)
print('Esta é a raiz: {}'.format(floor(raiz)))
print('\n\n\n')

# COMO VER OS CÓDIGOS E SEU MANUAL DE INFORMAÇÕES
# PESQUISE NO GOOGLE POR PYTHON > DOCS > SELECIONE A VERSÃO DO SEU PYTHON > LIBRARY REFERENCE
# PARA VER A VERSÃO, VÁ NO SEU PYTHON CONSOLE E DIGITE 'python --version'


# USANDO A BIBLIOTECA RANDOM
import random       # Ela gera números aleatórios
number = random.random()
print(number)

# Randomizando valores de 1 até 10
numero = random.randint(1,10)   #Utilize o 'randint(a,b)'
print(numero)

# Teste, no import, a lista de módulos que você pode importar por padrão.
#import # Aperte 'ctrl' + 'space'


# Voltando no site oficial do Python, vá na aba PyPi (Python package Index)
# 'Navegue entre projetos' encontre: https://pypi.org/search/
# Para teste, veja a biblioteca Emoji: https://pypi.org/project/emoji/

# Para fazê-la funcionar, é necessário instalar ela na sua IDE
# Então, digite o import emoji > clique sobre o nome emoji > vá na lâmpada vermelha e instale a biblioteca
import emoji #https://github.com/carpedm20/emoji/
print(emoji.emojize('Hello World :shushing_face:'))

# Para Desinstalar / ver os módulos externos, basta ir nas configurações e pesquisar 'interpreter'.
