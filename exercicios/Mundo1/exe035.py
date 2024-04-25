'''
    Desafio 035 - 
        Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas 
        podem ou nao formar um triangulo. 

        ->>  Para três segmentos fecharem um triângulo, cada lado deve ser menor que a soma dos outros dois.
'''

lado1 = float(input('Informe o comprimento de uma reta: '))
lado2 = float(input('Informe o comprimento da seguda reta: '))
lado3 = float(input('Informe o comprimento da terceira reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Essas 3 retas podem formar um triangulos.')
else: 
    print('Essas 3 retas NAO podem formar um triangulo.')