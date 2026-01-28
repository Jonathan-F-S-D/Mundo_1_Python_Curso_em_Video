### Manipulando Texto e Strings ###
frase = 'Curso em Video Python'
print(frase)
## Fatiamentos estudados
print(frase[9])                                 # Seleção de caracter específico
print(frase[9:13])                              # Seleção abrangente. Entre posições.
print(frase[1:15:2])                            # Seleção a cada dois.
print(frase[::2])                               # Do início ao fim a cada dois.

## Escrita de texto longo usa 3 aspas simples, no início e fim
print('''
Olá amigos da rede bobo. Venho hoje acompanhar o jogo do ano.
Mirassol de um lado, Curitiba do outro. Os times estão disputando
a grande Libertadores.
Quem sair daqui é campeão. Quem sair daqui leva a Taça para casa.
''')

### Tudo em Python é um objeto. Isso significa que, todo objeto pode levar .algumacoisa
## Análise

print(len(frase))                               # Tamanho da frase (21)
print(frase.count('o'))                         # Conta caracter específico
print(frase.count('o',0,13))   # Conta em determinado raio
print(frase.find('deo'))                        # Procura a palavra entre aspas e retorna sua posição.
print(frase.find('Android'))                    # Se não existe, retorna -1
print('Curso'in frase)                          # Retorna True or False

## Transformação

print(frase.replace('Python', 'Android'))   # Muda, neste print, uma palavra por outra
print(frase.upper())                            # Frase em Caixa ALta
print(frase.lower())                            # Frase em Caixa Baixa
print(frase.capitalize())                       # Primeira letra em maiúscula, o resto minúscula.
print(frase.title())                            # Todas as palavras com a primeira letra maiúscula

# Nova frase '   Aprenda Python   '

frase1 = '   Aprenda Python   '
print(frase1.strip())                           # Remove espaços, começo e fim
print(frase1.rstrip())                          # Remove os espaços finais
print(frase1.lstrip())                          # Remove espaços iniciais

## Divisão  -   Volta a Frase antiga

print(frase.split())                            # Corta as palavras nos espaços e cria grupos de palavras
juntinho = (frase.split())

## Junção

print('-'.join(juntinho))                       # Junta os grupos separados

##  Funções dentro de Funções
print(frase.upper().count('O'))
print(len(frase1.strip()))
print(frase.lower().find('python'))
print(juntinho[2] [3])                          # Seleciona o grupo, no primeiro [], e a posição, no segundo []
