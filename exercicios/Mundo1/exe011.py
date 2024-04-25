""" 
    Receber as dimensões de uma parede, exibir a dimensão recebida, 
    calcular a area da parede e quantos litros de tinta seriam gastos para pinta-la. 
    Considerar que 2 metros quadrados de parede, precisam de 1LT de tinta para ser pintado. 
"""

larguraParede = float(input('Largura da parede: '))
alturaParede  = float(input('Altura da parede: '))

areaParede = (alturaParede * larguraParede)
tinta = areaParede / 2


print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².\nPara pintar essa parede, você precisará de {}L de tinta'.format(larguraParede, alturaParede, areaParede, tinta))

