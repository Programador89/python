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

number = int(input('Informe um numero inteiro de 0 ate 9999: '))

unit = number // 1 % 10
dozen = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print('Analisando o numero {}'.format(number))
print('Unidade: {}'.format(unit))
print('Dezena: {}'.format(dozen))
print('Centena: {}'.format(hundred))
print('Milhar: {}'.format(thousand))


