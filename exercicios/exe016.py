"""
    Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
"""

import math

numeroReal = float(input('Digite um numero real qualquer: '))
print('O valor digitado foi {} e a sua posição inteira é {}'.format(numeroReal, math.floor(numeroReal)))


