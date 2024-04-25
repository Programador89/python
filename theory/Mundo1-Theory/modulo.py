# Utilizando modulo e puxando bibliotecas 

"""
    Em Python existem duas maneiras de importar bibliotecas. Da forma tradicional: 
        ->> Import + nome da biblioteca
    Ou importanto um item especifico dentro de uma biblioteca
        --> Fron + biblioteca + import + item da biblioteca.
"""

import math

numero = int(input('Digite um numero: '))

raiz = math.sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero, math.floor(raiz)))

