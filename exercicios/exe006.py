# Dobro, Triplo, Raiz quadrada

number = int(input('Digite um numero: '))
doble = number * 2
triple = number * 3
square_root = pow(number,(1/2))  #number ** (1/2)

print('O dobro de {} é {}'.format(number,doble))
print('O triplo de {} é {}'.format(number, triple))
print('A raiz quadrada de {} é {:.2f}'.format(number, square_root))