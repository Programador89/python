"""
    Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, 
    lendo o nome delas e escrevendo o nome do escolhido.
"""
import random
aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')

listaAlunos = [aluno1, aluno2, aluno3, aluno4]

print('O aluno escolhido foi o {}'.format(random.choice(listaAlunos)))