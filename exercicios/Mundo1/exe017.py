"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
    calcule e mostre o comprimento da hipotenusa. 
"""
import math 

cateto1 = float(input('Informe em inteiro o valordo primeiro cateto: '))
cateto2 = float(input('Informe em inteiro o valordo segundo cateto: '))

#hipotenusa = pow(cateto1, 2) + pow(cateto2, 2)
#print('A hipotenusa vai medir {:.2f}'.format(math.sqrt(hipotenusa)))

hipotenusa = math.hypot(cateto1, cateto2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))