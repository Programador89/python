'''
   Desafio 43- Calculadora IMC 
   
   Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

    – IMC abaixo de 18,5: Abaixo do Peso

    – Entre 18,5 e 25: Peso Ideal

    – 25 até 30: Sobrepeso

    – 30 até 40: Obesidade

    – Acima de 40: Obesidade Mórbida
    
    regra => Peso / (Altura * Altura)
'''

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)


if imc < 18.5:
    print('O IMC dessa pessoa é de: {:.1f} \nStatsus: Abaixo do seu peso ideal.'.format(imc))
elif imc >= 18.5 and imc < 25: 
    print('\nO IMC dessa pessoa é de: {:.1f} \nStatus: Peso Ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('O IMC dessa pessoa é de: {:.1f}\nStatus: Sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('\nO IMC dessa pessoa é de: {:.1f}\nstatus: Obesidade'.format(imc))
elif imc >= 40: 
    print('\nO IMC dessa pessoa é de: {:.1f}\nstatus: Obesidade morbida'.format(imc))
 



