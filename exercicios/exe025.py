'''
    Desafio 25: 
        Crie um programa que leia o nome de uma pessoa e diga se o nome possui "Silva" em qualquer parte dele.
'''

namePeople = input('Informe seu nome: ')
silvaName = 'Silva' in namePeople

print('Seu nome possui Silva? {}'.format(silvaName))