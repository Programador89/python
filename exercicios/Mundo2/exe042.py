'''
    Desafio 42 -
        Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

            – EQUILÁTERO: todos os lados iguais

            – ISÓSCELES: dois lados iguais, um diferente

            – ESCALENO: todos os lados diferentes

            Pre requisito -> Cada um dos lados tem que ser menor que a soma dos outros dois
'''

lado1 = float(input('Informe o comprimento de uma reta: '))
lado2 = float(input('Informe o comprimento de uma reta: '))
lado3 = float(input('Informe o comprimento de uma reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentod acima podem formar um triangulo!')
    if lado1 == lado2 == lado3:
        print('Este e um triangulo equilatero!')
    elif lado1 == lado2 != lado3:
        print('Este e um triangulo isosceles!')
    elif lado1 != lado2 != lado3 != lado1:
        print('Este e um triangulo escaleno!')
else:
    print('Os segmentos acima nao formam um triangulo')

