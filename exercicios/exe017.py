"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
    calcule e mostre o comprimento da hipotenusa. 
"""
import math

cateto1 = int(input('Informe em inteiro o valordo primeiro cateto: '))
cateto2 = int(input('Informe em inteiro o valordo segundo cateto: '))

hipotenusa = pow(cateto1, 2) + pow(cateto2, 2)

print('{:.2f}'.format(math.sqrt(hipotenusa)))