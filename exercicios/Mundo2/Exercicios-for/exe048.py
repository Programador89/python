'''
    Desafio 48: 
        Faça um programa que calcule a soma entre todos os numeros ímpares que são multipplos de 3
        e que se encontram no intervalo de 1 até 500.
'''
total = 0
contador = 0
for count in range(1,501,2):
    if count % 3 == 0:
        contador += 1
        total += count
print('A soma dos {} solicitado é: {}'.format(contador, total))