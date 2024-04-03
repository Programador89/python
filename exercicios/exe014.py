# Ao receber o valor da temperatura, converter para as demais escalas. S�o elas, Kelvin (K), Celsius (C), Fahrenheit (F)

temperatura = float(input('Informe a temperatura em C: '))
fahrenheit = temperatura * 1.8 + 32
kelvin = temperatura + 273.15

print('A temperatura de {:.1f}C corresponde a {:.1f}F (Fahreneit) e a {:.1f}K (Kelvin)!'.format(temperatura, fahrenheit, kelvin))

