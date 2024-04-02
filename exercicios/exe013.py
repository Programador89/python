# Reajuste salarial: Receber o valor atual do salário do funcionario e depois exibir reajuste de 15% no salário.

salario = float(input('Qual e o solario do funcionário: R$'))
percent = float(input('Informe o valor do desconto. Em porcentagem...'))
reajuste = salario + (salario * percent) / 100

print('Um funcionario que ganhava {:.2f}, com {:.2f}% de aumento, passa a receber {:.2f}'.format(salario, percent, reajuste)) 

