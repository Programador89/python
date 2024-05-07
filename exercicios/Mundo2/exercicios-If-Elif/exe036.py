'''
    Desafio 036: 
        Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. 
        O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
        
        Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo ser negado
'''

valorCasa = float(input('Informe o valor da casa R$'))
salario = float(input('Informe o valor do seu salário R$'))
anosPagamento = int(input('Quantos anos para concluir o pagamento: '))

prestacao = valorCasa / (anosPagamento * 12)
vlrMinimo = (salario * 30)/100

print('Para comprar uma casa de R${:.2f} em {} anos.'.format(valorCasa, anosPagamento), end='')
print(' a prestacao sera de R${:.2f}'.format(prestacao))

if prestacao <= vlrMinimo: 
    print('Emprestimo pode ser concedido!')
else: 
    print('Emprestimo negado!')