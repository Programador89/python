'''
    Desafio 34 - 
        Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.

        Para salario superiores a R$1.250,00, calcule um aumento de 10%
        Para inferiores ou iguais, o aumento e de 15%
'''

salario = float(input('Informe o seu salario atual: '))

if salario > 1250.00:
    aumento = (salario * 10)/100
    print('Seu aumento R${:.2f}. Seu salrio com reajuste e R${:.2f}'.format(aumento, salario + aumento))
elif salario <= 1250.00: 
    aumento = (salario * 15)/100
    print('Seu aumento R${:.2f}. Seu salrio com reajuste e R${:.2f}'.format(aumento, salario + aumento))