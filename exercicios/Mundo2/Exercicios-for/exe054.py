'''
    Desafio 54: 
        Crie um programa que leia o ano de nascimento de sete oessias. 
        No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. 
'''

jovem, velho, player = 0, 0, 0

for count in range(0 , 7):
    player += 1
    pessoa = int(input("{}ª pessoa, por favor, informe seu ano de nascimento: ".format(player)))

    ano = 2024 - pessoa
    if ano < 18:
        jovem += 1
    elif ano > 18:
        velho += 1
print("Foram {} pessoas maiores de idade, e {} manores".format(velho, jovem))

