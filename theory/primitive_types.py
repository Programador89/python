"""
    Os Tipos primitivos são:
        String, Int, Float, Boolean
        para adiciona-los:
            int(), bool(), float(), str()
"""

numberOne = input('Digite um numero:')
numberTwo = input('Digite outro numero:')
sum = float(numberOne) + float(numberTwo)

# sintaxe nova, aplicada a partir do Python 3, o format adiciona o conteúdo da variável no lugar do colchetes.
print('A soma entre {} e {}, vale {}'.format(numberOne, numberTwo, sum))

