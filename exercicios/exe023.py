'''
    Desafio 23:
        Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

        ex: 
        numero 1834
        unidade: 4
        dezena: 3
        centena: 8
        milhar: 1
'''

number = input('Informe um numero inteiro de 0 ate 9999: ')

print('Numero: {}'.format(number))
print('Unidade: {}'.format(number[3]))
print('Dezena: {}'.format(number[2]))
print('Centena: {}'.format(number[1]))
print('Milhar: {}'.format(number[0]))