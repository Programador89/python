'''
    Desafio 39
        Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
        
        - Se ele ainda vai se alistar ao servico militar.
        - Se e a hora de se alistar
        - Se ja passou do tempo do alistamento.
        
        Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo
        O programa tem que pegar o ano atual da maquina para realizar o calculo
'''

from datetime import datetime

yearOfBirth = int(input('Informe o ano do seu nascimento: '))

# Pegando o ano da maquina:
fullDate = datetime.now()
currentDate = fullDate.year

age = currentDate - yearOfBirth
yearOfEnlistment = yearOfBirth + 18

if age == 18:
    print('Sua idade e de {} anos. \nEsta na hora de se alistar.'.format(age))
elif age < 18:
    print('Sua idade e de {} anos. \nFaltam {} anos para o periodo do alistamento. \nO ano do seu alistamento sera {}'.format(age, (18-age), yearOfEnlistment))
else:
    print('Sua idade e de {} anos. \nPassaram {} anos do periodo de alistamento.\nSeu alistamento foi em {}'.format(age, (age-18), yearOfEnlistment))
