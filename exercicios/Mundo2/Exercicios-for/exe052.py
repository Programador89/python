'''
    Desafio 52: 
        Faça um programa que leia um numero interiro e diga se ele é ou não um número primo.
        Numros Primos: são divisíveis por 1 e por ele mesmo
        
        if(entrada % )

        print('{} '.format(num), end=' ')
'''

num_primo = int(input('Digite um numero: '))
total = 0
for count in range(1, num_primo + 1):
    if num_primo % count == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(count), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num_primo, total))
if total == 2:
    print('Numero primo')
else:
    print('Numero nao e primo')



