# Conversor de moedas - crie um programa que informe quantos doláres podem ser comprados com o valor em real informado na tela.

realNaCarteira = int(input('Quanto dinheiro você tem na carteira? '))

valorDolar  = 5.02
valorEuro   = 5.41
valorLibra  = 6.33

compraDolar = (realNaCarteira / valorDolar)
compraEuro  = (realNaCarteira / valorEuro)
compraLibra = (realNaCarteira / valorLibra)

print('Com R${:.2f} você pode comprar US${:.2f}'.format(realNaCarteira, compraDolar))
print('Com R${:.2f} você pode comprar €${:.2f}'.format(realNaCarteira, compraEuro))
print('Com R${:.2f} você pode comprar £${:.2f}'.format(realNaCarteira, compraLibra))
