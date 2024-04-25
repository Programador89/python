'''
    Desafio 28 - 
    Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca 
    para o usuario tentar descobrir qual foi o numero escolhido pelo computador.

    - O programa devera escrever na tela se o usuario venceu ou perdeu.
'''
from random import randint
from time import sleep

number_choise = int(input('Qual numero inteiro entre 0 e 5 eu pensei. Podes adivinhar humano? '))
print('PROCESSANDO...')
sleep(2)
number_random = randint(0,5)

if number_choise == number_random:
    print('Acertou ordinario!! Eu pensei no numero {}'.format(number_random))
else:
    print('Sabe de nada inocente!!!! Eu pensei no numero {}'.format(number_random))
