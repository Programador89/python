"""
    O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
    Faça um programa que leia o nome dos quatro alunos e moste a ordem sorteada. 
"""
from random import sample

alunos = ['Rafael', 'Larissa', 'Joao', 'Elisa']
sorteio = sample(alunos, 4)

print('A ordem escolhida para apagaro quadro foi: {}'.format(sorteio))
