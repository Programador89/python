'''
    Desafio 55: 
        Faça um programa que leia o peso de 5 pessoas. 
        No final, mostre qual foi o maior e o menor peso lidos.
'''

cont_pessoa = 1
for count in range(0,5):
    peso = float(input("Informe da pessoa {}: ".format(cont_pessoa)))
    if