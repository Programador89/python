'''
    Desafio 50: 
        Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que
        forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

'''total = 0
cont = 0
for count in range(0,6):
    num1 = int(input("Informe um numero inteiro: "))
    if num1 % 2 == 0:
        total += num1
        cont += 1
print("A soma dos numeros inteiros digitados é {}".format(total))  '''  


# Informe o valor de 10 produtos com saldo maior que 0 e some o valor de todos os produtos com preço acima de R$35,00

total, cont = 0, 0
for count in range(0,10):
    valor1 = float(input("Informe o valor do produto: "))
    if valor1 > 35:
        total += valor1
        cont += 1
input("Valor total dos produtos com preço individual acima de R$35: {:.2f}".format(total))
