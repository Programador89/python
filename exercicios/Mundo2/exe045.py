# Exercício 45: Crie um programa que faça o computador jogar Jokenpô com você.
import time
import random

print('''
[0] Pedra
[1] Papel
[2] Tesoura''')

jogada = int(input('Qual e a sua jogada? '))

time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')


num_Ale = random.randint(0,2)

print('-='* 11)
if jogada == 0 and num_Ale == 0:
    print('''Draw Game!!!\n
Player -> Rock
Machine -> Rock''')
elif jogada == 0 and num_Ale == 1:
    print('''You Lose!!\n
Player -> Rock
Machine -> Paper''')
elif jogada == 0 and num_Ale == 2:
    print('''You Win!!!\n
Player -> Rock
Machine -> scissors''')
    
if jogada == 1 and num_Ale == 0:
    print('''You Win!!!!\n
Player -> Paper
Machine -> Rock''')
elif jogada == 1 and num_Ale == 1:
    print('''Draw Game!!\n
Player -> Paper
Machine -> Paper''')
elif jogada == 1 and num_Ale == 2:
    print('''You Lose!!!\n
Player -> Paper
Machine -> scissors''')

if jogada == 2 and num_Ale == 0:
    print('''You Lose!!!!\n
Player -> Scissors
Machine -> Rock''')
elif jogada == 2 and num_Ale == 1:
    print('''You Win!!\n
Player -> Scissors
Machine -> Paper''')
elif jogada == 2 and num_Ale == 2:
    print('''Draw Game!!!\n
Player -> Scissors
Machine -> scissors''')

else:
    print('Valor informado invalido. Preencha com um dos valores do enunciado!')
print('-='* 11)