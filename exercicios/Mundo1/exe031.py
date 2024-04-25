'''
    Desafio 31 - 
        Desenvolva um programa que pergunte a distancia de uma viagem em km.
        Calcule o preco da passagem, cobrando R$0,50 por km para vaigens de ate 200km e 
        R$0,45 para viagens mais longas
'''

distancia = float(input('Informe a distancia da viagem: '))
if distancia <= 200: 
    valor_passagem = (distancia * 0.50)
    print('Para uma viagem de {}km, o valor da passagem é R${:.2f}'.format(distancia, valor_passagem))
else:
    valor_passagem2 = (distancia * 0.45)
    print('Para uma viagem de {}km, o valor da passagem é R${:.2f}'.format(distancia, valor_passagem2))