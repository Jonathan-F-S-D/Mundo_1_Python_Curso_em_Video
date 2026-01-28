'''
                            Manipulando Texto

    *Parte Teorica*
- O que é uma cadeia de textos?

    Abaixo, isto é uma cadeia de texto
    'Curso em Video Python'             # Tudo em aspas simples ou duplas é texto

    frase = ('Curso em Video Python')   # Essa é a forma de atribuição de uma variável dentro de uma String (str)
    # Ele coloca essa variável dentro da memória do computador, dentro de pequenos espaços retangulares.
    # Esses espaços começam do número 0 (sendo o 'C' do Curso) e os espaços são contados.
    #Sabendo disso, é possível realizar algumas operações em texto.

     * Fatiamento
     # Fatiamento significa pegar alguns pedaços específicos da frase.

     EX: frase[9]   - Fará com que o programa marque o Nono caracter da frase 'Curso em Video Python', no caso, o 'V' (lembra que a contagem começa no 0)
     EX.2: frase[9:13]  - Começará o fatiamento na Nona posição e parará na 12ª posição (Sim, ele exclui o 13 e para 1 casa antes do fatiamento) ('Vide')
     EX:.3 frase [9:21] - Em nosso exemplo ('Curso em Video Python'), temos 20 posições (contando o 0).
                          Neste fatiamento, não há 21 posições, logo, o sistema mostrará a frase fatiada até o final ('Video Python').
                          Esta forma não é a mais otimizada possível.

     EX:.4 frase[9:21:2]    - Este segundo valor (:2) significa que o sistema mostrará, dentro do fatiamento de '9:12', todos os caracteres pulando de 2 em 2
                              A frase é 'Video Python', pulando de dois em dois ficará 'VdoPto'
                              Interpretando: [9:21:2]: vai fatiar da casa 9 até 21, pulando de dois em dois.
     EX:.5 frase[:5]   - O fatiamento ocorrerá do início da frase (posição 0) até o 4 (porque a posição 5 não conta)
                          Sendo a resposta igual a 'Curso'.

     EX:.6 frase[15:]   - Mesmo fatiamento do anterior, porém, ele começará da posição 15 e irá até o final ('Python)
     EX:.7 frase[9::3]  - O sistema fatiará a partir da posição 9, até o final, pulando de três em três digitos.
                          ('VePh')


     * Análise
     # A Análise serve para saber, por exemplo, 'Quantos caracteres tem a String?', 'Qual a primeira letra?', 'Qual a última letra?', 'Quantas palavras tem a frase?'...

     len(frase)        - Serve para retornar o comprimento da frase (len() = comprimento)
     frase.count('o')  - Serve para contar, no caso, quantos 'o' tem na frase inteira (Maiúsculas e minúsculas são diferentes)
     frase.count('o',0,13) - Contagem de letras 'o' no fatiamento (do 0 até o 12 = 'Curso em Vide')

     frase.find('deo')   - Retornará em que momento encontrará o 'deo' na frase. No caso, na posição 11 da frase 'Curso em Vídeo Python'.
     frase.find('Android')  - Se você pesquisa uma palavra que não há na frase buscada, o sistema retornará -1 para te avisar que a palavra buscada não se encontra.
     'Curso'infrase   - Ele dirá se há a a palavra na frase. No caso, retornaria 'True'.

     * Transformação
     Via de regra, uma lista de string é imutável; não há possibilidade de de mudança.
     Porém, é possível mudar ela por meio de métodos (não modificando sua essência).

     frase.replace('Python','Android')  - Substituirá a palavra Python por Android (Ele não substitui diretamente a string, mas para apresentação apenas)
     frase.upper()  - transforma todas as letras minúsculas em maiúsculas, de toda a frase/string.
     frase.lower() - Transforma todas as letras minúsuclas em Maiúsculas.
     frase.capitalize() - Colocará, primeiro, todos os caracteres em minúsuculo, porém, a primeira letra da string ficará em Caixa Alta.
     frase.title()  - Todas as palavras ficarão com a primeira letra em Caixa Alta.

     Nova string usada agora: '   Aprenda Python  '     # Sim, é proposital o espaço

     frase.strip()  - Ele removerá todos os espaços inúteis (espaços antes da frase e depois dela).
     frase.rstrip() - Remove todos os espaços existentes na direita da frase (os últimos espaços) são deletados
     frase.lstrip() - Remove todos os espaços da esquerda (os iniciais).

     * Divisão
     A Divisão serve para separar frases e palavras em blocos
     (Voltaremos a usar a frase 'Curso em Vídeo Python')

     frase.split()  - Criará blocos de palavras aonde há espaços. Essa divisão ficaria assim: ('Curso','em','Vídeo','Python')
                      Essa quebra faz com que todos se tornem blocos separados, e cada bloco possue um número diferente de digitos,
                      ('Curso'[0:5],'em[0:2]','Vídeo[0:5]','Python[0:6]')

     * Junção
     Este é o contrário da Divisão. Este juntará as palavras/frases.

     '-'.join(frase)    - Juntará as palavras com, no caso, '-' no lugar dos traços.


# Início dos testes
'''

frase = 'Curso em Vídeo Python'
print(frase)

### Fatiamento

print(frase[3])
print(frase[9:21])
print(frase[:15:2])
print(frase[1::3])

### Análise
print(len(frase))   # Número de dígitos (Inicia do 0 e conta os espaços)
print(frase.count('V'))
print(frase.count('o',0,21))
print(frase.find('Pyt'))    # Mostra a posição que se encontra o pesquisado
print(frase.find('Android')) # -1 é equivalente ao 'Não encontrado'
print('em'in(frase))

### Facilidade Fudida para printar textos longos com 1 print
# Escreva o que quiser dentro do print, com parágrafos e tudo mais e coloque aspas simples (triplas), no começo e no final do texto.

print(''' 
Eu sou o cavaleiro da Távola Redonda, cujo o objetivo é restaurar a ordem e o caos da terra nórdica de meu povo.
Com o Cálice em mãos, retiro minha espada da bainha e coloco-a sobre os raios do sol.
- Que seja purificada com a graça dos céus em minha jornada de restauração. Que Deus nos abençoe.
''')

### Transformação

print(frase.upper().count('PYTHON'))
print(frase.lower().find('so'))
frase2 = '   Aprenda Python   '
print(len(frase2))
print(len(frase2.strip()))
print(frase.replace('Python', 'Android'))

### Divisão
frase3 = 'Curso em Vídeo Python'
dividido = frase3.split()
print(frase3,'/',dividido[0:3])     # Código de inclusão de partes
print(frase3,'/',dividido[2][2])    # Mostra a parte 2 e a posição do caracter 2
                                    # Lembre que começa no 0 a contagem