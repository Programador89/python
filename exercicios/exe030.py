'''
    Desafio 30 - 
        Crie um programa que leia um numero inteiro e mostre na tela se ele e PAR ou IMPAR.
'''

number = int(input('Digite um numero inteito: '))

if number % 2 == 0:
    print('{} - numero PAR'.format(number))
else:
    print('{} - numero IMPAR'.format(number))