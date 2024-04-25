'''
    Desafio 29 - 
        Escreva um programa que leia a velocidade de um carro. 

        Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
        A multa vai custar R$7,00 por cada km acima do limite.
'''

veloc = float(input('Informe a velocidade do carro: '))

if veloc > 80:
    multa = (veloc - 80) * 7
    print('Velocidade excedida. Motorista multado em {:.2f}'.format(multa))
print('Dentro do limite de velocidade, pode seguir viagem.')
