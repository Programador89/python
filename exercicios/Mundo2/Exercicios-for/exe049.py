'''
    Desafio 49: 
        Refaça o desafio 009, mostrando a tabuada de um numero que o usuário escolher,
        só que agora utilizando o laço FOR
'''
number = int(input('Digite um numero para ver sua tabuada: '))
contador = 0
total = 0
for count in range(1,11):
    contador += 1
    total = number * contador
    print('{} x {} = {}'.format(number,contador,total))