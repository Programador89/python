'''
    Desafio 22:
        Crie um programa que leia o nome completo de uma pessoa e mostre:
            - o nome com todas as letras maiusculas
            - O nome com todas as letras minusculas
            - Quantas letras ao todo (sem considerar espacos) -> A FAZER 
            - Quantas letras tem o primeiro nome
'''

name = str(input('Informe seu nome completo: ')).strip()

nameUpper = name.upper()
nameLower = name.lower()
nameCurto = name.strip()
espacoBranco = name.split(' ')

print('Todas as letras maiusculas {}'.format(nameUpper))
print('Todas as letras minusculas {}'.format(nameLower))

print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))

print(espacoBranco)
print('O primeiro nome tem {} letras'.format(len(espacoBranco[0])))
