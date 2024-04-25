# Receber o preço de um produto e mostrar seu novo preço com 5% de desconto

valor = float(input('Qual é o valor do produto: R$'))

desconto = (valor * 5)/100
valorFinal = valor - desconto

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custarR${:.2f}'.format(valor, valorFinal))
