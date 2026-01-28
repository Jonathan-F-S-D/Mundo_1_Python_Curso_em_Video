'''             Aula 10 - Condições

    *   Condições são regras, comando, que sustentam a programação
        e a guiam por um caminho ou outro.

    Imagine que eu tenho um carro com um percurso, com um ponto para se chegar.
    Há, necessariamente, um caminho que o carro pode fazer, imaginando um único meio.

    Sendo assim, teríamos, por exemplo, um código descrito assim;:

    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.para()

    Essa estrutura se chama 'Sequência'.

Todos os exercícios foram feitos, até agora, em sequência.
Necessariamente, todos os comandos até aqui, precisavam ser executados um após o outro.

    Agora, se este mesmo carro possuir dois caminhos distintos, duas possibilidades, que levam ao mesmo destino,
    haverá dois códigos, o da "direita" e o da "esquerda".

    Imaginêmos assim:
    carro.siga()

    Se carro.direita():
        carro.direita()
        carro.siga()
        carro.esquerda()
        carro.siga()
        carro.direita()                 # Tudo isso é um Bloco de Comandos
        carro.siga()                    # No python, apenas precisa conceder um espaço, com tab, para escrever dentro de um If ou Else. (Tabulação)
        caro.esquerda()                 # Os dois comandos nunca poem acontecer simultaneamente; apenas um caminho pode ser escolhido.
        carro.siga()
        carro.esquerda()
        carro.siga()
        carro.para()

    Senão:
        carro.esquerda()
        carro.siga()
        carro.direita()
        carro.siga()
        carro.direita()
        carro.siga()
        carro.para()

    carro.fim()


Isto não é assombroso. Na verdade, é o nosso querido If e Else

    * o if (se) vem primeiro e funciona da mesma forma que o exemplo acima
    if <= 3:
        print('Número pequeno')

    * já o else serve como oposição a escolha do if
    else:
        print('Número grande!')


    * C O N D I Ç Ã O
    if carro.esquerda():
        bloco True
    else:
        bloco False

######### EXEMPLO ##########

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é bem novo!')  # Ou ele executará esta linha.
else:
    print('Seu carro está bem velho')   # Ou executará esta daqui
print('--F I M --')

#### C O N D I Ç Ã O    S I M P L I F I C A D A ####

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo<=3 else 'carro velho')  # Não é muito visual e pouco inteligível. Porém, funciona igual ao anterior.
print('-- F I M --')

'''
