'''
    Desafio 38
        Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
        
        - O primeiro valor e maior
        - O segundo valor e maior   
        - Nao existe valor maior, os dois sao iguais
'''

numberOne = int(input('Informe o primeiro valor inteiro: '))
numberTwo = int(input('Informe o segundo valor inteiro: '))

if numberOne > numberTwo:
    print('O primeiro valor e maior')
elif numberTwo > numberOne:
    print('O segundo valor e maior')
else:
    print('Nao existe valor maior, os dois sao iguais')
