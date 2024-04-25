# Em Python, o aninhamento de código refere-se à organização hierárquica de blocos de código dentro de outros blocos.

tipoPele = str(input('Qual tonalidade de pele voce se identifica: Pardo, Negro, Amarelo, Branco ou Indigena ')).capitalize()

if tipoPele[0] == 'B':
    print('Voce faz parte de 47.51% de brasileiros que se identificam como brancos.')
elif tipoPele[0] == 'P':
    print('Voce faz parte de 43.42% de brasileiros que se identificam como pardos.')
elif tipoPele[:1] == 'Pr':
    print('Voce faz parte de 7.52% de brasileiros que se identificam como pretos.')
elif tipoPele[0] == 'A':
    print('Voce faz parte de 1.1% de brasileiros que se identificam como amarelos.')
elif tipoPele[0] == 'I':
    print('Voce faz parte de 0.42% de brasileiros que se identificam como indigenas.')
else: 
    print('Desculpe nao intendi o que voce escreveu, selecione apenas uma das respostas validas.')


