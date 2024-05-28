'''
    Desafio :
        Desenvolva um programa que leia o primeiro termo e a razão de uma PA(Progressão Aritmética). 
        No final, mostre os 10 primeiros termos dessa prograssão.
'''

entrada = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
enesimo = entrada + (10-1) * razao
for count in range(entrada, enesimo + razao, razao):
    print(count)
    
    
