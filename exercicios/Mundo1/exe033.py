'''
    Desafio 33 - 
        Faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor
'''

numb1 = int(input('Informe o primeiro numero: '))
numb2 = int(input('Informe o segundo numero: '))
numb3 = int(input('Informe o terceiro numero: '))

if numb1 > numb2 and numb1 > numb3:
    print('O maior numero digitado foi {}'.format(numb1))
elif numb2 > numb1 and numb2 > numb3:
    print('O maior numero digitado foi {}'.format(numb2))
elif numb3 > numb1 and numb3 > numb2:
    print('O maior numero digitado foi {}'.format(numb3))

if numb1 < numb2 and numb1 < numb3:
    print('O menor numero digitado foi {}'.format(numb1))
elif numb2 < numb1 and numb2 < numb3:
    print('O menor numero digitado foi {}'.format(numb2))
elif numb3 < numb1 and numb3 < numb2:
    print('O menor numero digitado foi {}'.format(numb3))