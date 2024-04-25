"""
    Exercicio Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por 
    um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, 
    sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

kmPercorrido = float(input('Informe a quantidade de KM rodado: '))
diasAluguel = float(input('Quantos dias ele foi alugado? '))

precoPagar = (60 * diasAluguel) + (kmPercorrido * 0.15)

print('O valor a pagar no aluguel do carro é de: {:.2f}'.format(precoPagar))

