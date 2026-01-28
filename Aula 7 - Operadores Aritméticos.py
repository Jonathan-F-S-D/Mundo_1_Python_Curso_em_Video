# Revisão da última aula

n1 = int (input('Digite um número inteiro: '))
n2 = int (input('Digite um segundo número inteiro: '))
soma = n1 + n2
print ('A soma de {} e {} é igual a {}'.format(n1, n2, soma))

# Principais operadores

# +, -, *, / = Operadores simples

# ** (potência), // (Divisão inteira), % (Resto da Divisão)

#Exercícios para teste (UTILIZE O IDLE SHELL PARA MELHOR APRENDIZADO)
#Ou Abra o Python Console, aqui na IDE mesmo, e faça suas contas.

5 + 3 * 2 == 11 #True

3 * 5 + 4**2 == 31 #True

3 * (5+4)**2 == 243 #True

##Teste de códigos
nome = input ('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

# Mostrar o nome em 20 caracteres
print('Prazer em te conhecer {:20}!'.format(nome)) #Ele escreve seu nome em 20 espaços

# Alinhamento à direita
print('Prazer em te conhecer {:>20}!'.format(nome))

# Alinhamento à esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))

# Alinhamento Centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))

# Mostrar o nome em 20 caracteres, preenchendo os espaços vazios com o o Caracter desejado.
print ('Prazer em te conhecer {:¨^20}!'.format(nome))

##
# Lendo dois números inteiros e realizando cáculos

num1 = int(input('Digite um valor para ser calculado várias vezes: '))
num2 = int(input('Digite um segundo valor: '))
print('A soma entre os números é igual a {}'.format(num1+num2))
print('A subtração de ambos é igual a {}'.format(num1-num2))
print('A divisão entre os dois será igual à {}'.format(num1/num2))
print('Sua multiplicação implicará neste resultado: {}'.format(num1*num2))
print('Com potência 2, o valor final, unidos, será igual a: {}'.format((num1+num2)**2))
print('Sua Divisão inteira será equivalente à: {}'.format(num1//num2))
print('Por fim, o resto desta divisão será igual a {}'.format(num1%num2))

#Deixando mais fácil a programação com .format() e delimitação de valores

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite um segundo valor: '))
s = numero1 +numero2
sub = numero1 - numero2
m = numero1 * numero2
d = numero1 / numero2
di = numero1 // numero2
rd = numero1 % numero2
print('A soma é {}, a subtração é {}, o produto é {}.'.format(s,sub,m))
print('A divisão é {}, divisão inteira resulta em {} e o resto da divisão é {}.'.format(d,di,rd))

# Deixando mais fácil com a quebra da linha, na codificação, mas não na apresentação.
print('A soma é {}, a subtração é {}, o produto é {}'. format(s,sub,m), end='') # o ,end='' é a forma de juntar o print seguinte para que ambos apareçam na mesma linha.
print('A divisão é {:.3f}, divisão inteira em {} e o resto da divisão é {}'.format(d,di,rd)) #o valor
# posto em {:.3f} significa que, após a vírgula, mostrará naquele valor apenas 3 casas decimais, mesmo que o resultado possua mais.

# Quebra de linha no meio do print
print('A soma é {}, \n a subtração é {}, \n o produto é {}.'. format(s,sub,m), end='') # \n (contra barra + n) faz a quebra do print aonde fora colocado, sem a necessidade de criar diversos print.
print('A divisão é {:.3f}, divisão inteira em {} e o resto da divisão é {}'.format(d,di,rd))

9**(1/2)