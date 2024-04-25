# Calcular a média aritmética entre 2 valores

vNota1 = float(input('Digite a primeira nota: '))
vNota2 = float(input('Digite a segunda nota: '))

media = (vNota1 + vNota2)/2
print('A media entre {:.1f} e {:.1f} é {:.1f}'.format(vNota1, vNota2, media))

if(media <= 7):
    print('Reprovado! \nMédia abaixo de 7.0')
else:
    print('Aprovado!\nMédia maior que 7.0')