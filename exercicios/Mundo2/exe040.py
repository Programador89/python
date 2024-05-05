'''
    Desafio 40 -
        Crie um programa que leia duas notas do aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
        a média atingida.

        – Média abaixo de 5.0: REPROVADO

        – Média entre 5.0 e 6.9: RECUPERAÇÃO

        – Média 7.0 ou superior: APROVADO

'''

nota1 = float(input('Informe a nota da P1: '))
nota2 = float(input('Informe a nota da P2: '))

media = (nota1 + nota2)/2

if media < 5.0:
    print('Média abaixo de 5.0: REPROVADO')
elif 5.0 >= media <= 6.9:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO')
else:
    print('Meda 7.0 ou superior: APROVADO!')
