'''
    Desafio 032 - 
        Faca um programa que leia um ano qualquer e mostre se ele e Bissexto
'''
from datetime import date

ano = int(input('Informe um ano qualquer: Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
elif ano % 100 != 0:
    print('O ano {} nao e bissesto.'.format(ano))