'''
    Desafio 27: 
        Faca um programa que o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

        ex: Rafael Dantas   
        Primeiro = Rafaeel
        ultimo = Dantas
'''

name = str(input('Digite seu nome completo: ')).strip()
nome = name.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu ultimo nome e {}'.format(nome[len(nome)-1]))