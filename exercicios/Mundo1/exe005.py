"""
    Faça um programa que leia um numero inteiro 
    e mostre na tela o seu secessor e seu antecessor
"""

entrada = int(input('Digite um numero: '))
antes = entrada - 1
depois = entrada + 1 

print('Analisando o numero {} seu antecessor é {} e seu sucessor é {}'.format(entrada, antes, depois))