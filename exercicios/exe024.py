'''
    Desafio 24 
        Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com nome "Santo"
'''

city = str(input('Informe o nome da sua cidade: ')).strip()
print(city[:5].upper()=='SANTO')