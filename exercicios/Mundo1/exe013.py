# Reajuste salarial: Receber o valor atual do salário do funcionario e depois exibir reajuste de 15% no salário.

salario = float(input('Qual e o salario do funcionário: R$'))
percent = float(input('Valor do aumento em %: '))
reajuste = salario + (salario * percent) / 100

print('Um funcionario que ganhava {:.2f}, com {:.2f}% de aumento, passa a receber {:.2f}'.format(salario, percent, reajuste)) 

