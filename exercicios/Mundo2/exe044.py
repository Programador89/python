'''
    Exercício 44: 
        Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

            – à vista dinheiro/cheque: 10% de desconto

            – à vista no cartão: 5% de desconto

            – em até 2x no cartão: preço formal 

            – 3x ou mais no cartão: 20% de juros
'''

preco = float(input('Preço das compras: R$'))
print('''
      FORMAS DE PAGAMENTO: 
      [1] à vista dinheiro/PIX
      [2] à vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão
      ''')

option = int(input('Informe a opção desejada: '))

if option == 1: 
    desconto = preco * 0.10
    valorFinal = preco - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} com nosso cupom de desconto de 10%'.format(preco, valorFinal))
elif option == 2: 
    desconto = preco * 0.05
    valorFinal = preco - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} com nosso cupom de desconto de 5%.'.format(preco, valorFinal))
elif option == 3: 
    valorFinal = preco / 2
    print('Sua compra de R${:.2f} foi parcelada em 2x sem juros, no valor de R${:.2f} por parcela.'.format(preco, valorFinal))
elif option == 4: 
    parcela = int(input('Informe a parcela desejada (3 à 10x - com juros): '))
    if parcela == 3:
        juros = preco * 0.20
        valorFinal = (preco + juros)/parcela
        total = preco + juros
        print('Sua compra de R${:.2f} foi parcelada em {}x com juros, no valor de R${:.2f} por parcela. Total a pagar{:.2f}'.format(preco,parcela,valorFinal,total))
    elif parcela == 4:
        juros = preco * 0.20
        valorFinal = (preco + juros)/parcela
        total = preco + juros
        print('Sua compra de R${:.2f} foi parcelada em {}x com juros, no valor de R${:.2f} por parcela. Total a pagar{:.2f}'.format(preco,parcela,valorFinal,total))
    elif parcela == 5:
        juros = preco * 0.20
        valorFinal = (preco + juros)/parcela
        total = preco + juros
        print('Sua compra de R${:.2f} foi parcelada em {}x com juros, no valor de R${:.2f} por parcela. Total a pagar{:.2f}'.format(preco,parcela,valorFinal,total))
    elif parcela == 6:
        juros = preco * 0.20
        valorFinal = (preco + juros)/parcela
        total = preco + juros
        print('Sua compra de R${:.2f} foi parcelada em {}x com juros, no valor de R${:.2f} por parcela. Total a pagar{:.2f}'.format(preco,parcela,valorFinal,total))
    elif parcela == 7:
        juros = preco * 0.20
        valorFinal = (preco + juros)/parcela
        total = preco + juros
        print('Sua compra de R${:.2f} foi parcelada em {}x com juros, no valor de R${:.2f} por parcela. Total a pagar{:.2f}'.format(preco,parcela,valorFinal,total))
    elif parcela == 8:
        juros = preco * 0.20
        valorFinal = (preco + juros)/parcela
        total = preco + juros
        print('Sua compra de R${:.2f} foi parcelada em {}x com juros, no valor de R${:.2f} por parcela. Total a pagar{:.2f}'.format(preco,parcela,valorFinal,total))
    elif parcela == 9:
        juros = preco * 0.20
        valorFinal = (preco + juros)/parcela
        total = preco + juros
        print('Sua compra de R${:.2f} foi parcelada em {}x com juros, no valor de R${:.2f} por parcela. Total a pagar{:.2f}'.format(preco,parcela,valorFinal,total))
    elif parcela == 10:
        juros = preco * 0.20
        valorFinal = (preco + juros)/parcela
        total = preco + juros
        print('Sua compra de R${:.2f} foi parcelada em {}x com juros, no valor de R${:.2f} por parcela. Total a pagar{:.2f}'.format(preco,parcela,valorFinal,total))
else:
    print('Opcao invalida, tente novamente. O valor da sua compra e: R${:.2f}'.format(preco))
    