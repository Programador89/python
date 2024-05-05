'''
    Desafio 41 -
         A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
         sua categoria, de acordo com a idade:

            – Até 9 anos: MIRIM

            – Até 14 anos: INFANTIL

            – Até 19 anos: JÚNIOR

            – Até 25 anos: SÊNIOR

            – Acima de 25 anos: MASTER
'''

from datetime import datetime

anoNasc = int(input('Informe o ano do seu nascimento: '))

anoAtual = datetime.now()
anoCorte = anoAtual.year
idade = anoCorte - anoNasc

if idade <= 9:
    print('Sua idade é {} anos. Ate 9 ano: categoria Mirim'.format(idade))
elif idade <= 14:
    print('Sua idade é {} anos. Até 14 anos: INFANTIL'.format(idade))
elif idade <= 19:
    print('Sua idade é {} anos. Até 19 anos: JÚNIOR'.format(idade))
elif idade <= 25:
    print('Sua idade é {} anos. Até 25 anos: SÊNIOR'.format(idade))
else:
    print('Sua idade é {} anos. Acima de 25 anos: MASTER'.format(idade))
