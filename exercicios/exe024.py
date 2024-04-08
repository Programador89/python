'''
    Desafio 24 
        Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com nome "Santo"
'''

city = input('Informe o nome da sua cidade: ')
nomeSanto = 'Santo' in city

print('Sua cidade comeca com a palavra Santo? {}'.format(nomeSanto))