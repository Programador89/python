"""
    Faça um programa que leia um angulo qualquer e mostra na tela o valor do: Seno, Cosseno, tangente desse angulo.
"""
<<<<<<< HEAD
from math import sin,cos,tan, radians

angulo = float(input('Digite o angulo que voce deseja: '))

#convertendo o valor do input para radiano e calculando o seno com a funcao math.sin
seno = sin(radians(angulo)) 
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cos))
print('O angulo de {} tem o tangente  de {:.2f}'.format(angulo, tan))
=======
import math

ang = float(input('Informe um angulo: '))
rad = math.radians(ang)

sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('O valor do seno do angulo informado é {:.2f}'.format(sen))
>>>>>>> 583406a0c68bbb68bfbb078f7c18cfd23e172fdb
