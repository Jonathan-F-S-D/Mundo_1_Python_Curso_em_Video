# Exercício 26 Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('Sua frase é: {}.\nEla possui {} letras A.\nO primeiro A que aparece está na posição: {}\nA última está na posição: {}'.format(frase,frase.count('A' and 'Ã'),frase.find('A' and 'Ã')+1, frase.rfind('A' and 'Ã')+1))
# As somas (+1) servem para mostrar a posição ao usuário das letras.
# Nós sabemos que o find mostra 1 posição antes da letra procurada, logo o +1 serve para indicar exatamente a posição da letra.
# O 'and' serve como adição ("... e também...")
# 'Usuário é a pior raça que tem. Ele fará coisas para o seu programa parar de funcionar' - Guanabara