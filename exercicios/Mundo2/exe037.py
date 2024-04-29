'''
    Desafio 037
        Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao:
        
        - 1 para binario
        - 2 para octal
        - 3 para hexadecimal
        
        o programa vai ler a resposta e converter o numero digitado enteriormente conforme a base informada pelo usuario
'''

number = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversao: ')
print('[1] converter para BINARIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')

option = int(input('Sua opcao: '))

if option == 1:
    print('{} convertido para BINARIO e igual a {}'.format(number, bin(number)[2:]))
elif option == 2:
    print('{} convertido para OCTAL e igual a {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(number, hex(number)[2:]))
else:
    print('O valor informado nao e valido!')