"""
    Faça um programa que leia um angulo qualquer e mostra na tela o valor do: Seno, Cosseno, tangente desse angulo.
"""
import math

ang = float(input('Informe um angulo: '))
rad = math.radians(ang)

sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('O valor do seno do angulo informado é {:.2f}'.format(sen))